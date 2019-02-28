import pandas as pd
import Queries_FileHandling as H_GA
from mysql.connector import errorcode
import mysql.connector
import DataAccess as DA
import LogGen as logging
class SQLToDataFrames:
    Db_Data = []
    Db_Colnames = []
    Db_Sql_Tables = []


    def createDF(self,DB_sql_cmds):

        try:
            for db_query in DB_sql_cmds:
                self.Db_Data.append(DA.DB_Connection().query(db_query))
                self.Db_Colnames.append(DA.DB_Connection().query_col_names(db_query))


        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.logger.info("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.logger.info("Database does not exist")

            elif Exception:
                logging.logger.error("QUERY : %s  EXECUTED and Row Data not Fetched ", db_query)
                logging.logger.error("QUERY : %s NOT EXECUTED and Column Name not Fetched", db_query)
        else:
                logging.logger.info("Database Connected")
                logging.logger.info("QUERY : %s  EXECUTED and Row Data Fetched ", db_query)
                logging.logger.info("QUERY : %s  EXECUTED and Column Name Fetched ", db_query)

        for itr in range(0,len(self.Db_Data)):
            self.Db_Sql_Tables.append(pd.DataFrame(self.Db_Data[itr],columns=self.Db_Colnames[itr]))
        return self.Db_Sql_Tables

    def monthDF(self,DataFrame,monthNum):

            monthDFs=DataFrame[pd.DatetimeIndex(DataFrame['examDate']).month == monthNum]
            monthDFs['Total']=monthDFs['English']+monthDFs['Tamil']+monthDFs['Maths']+monthDFs['Science']+monthDFs['Social']
            monthDFs.sort_values("Total", ascending=False, inplace=True)
            monthDFs.insert(len(monthDFs.columns), 'Rank', range(1, 1 + len(monthDFs)))
            return monthDFs



