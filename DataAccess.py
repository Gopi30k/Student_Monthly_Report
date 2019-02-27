import logging
import mysql.connector as MySQL
class DB_Connection:
    def __init__(self):
        self.db=MySQL.connect(host="localhost", user="root", password="root", db="Student_monthly_report_v2")
        self.crsr = self.db.cursor()


    def query(self,query):
        self.crsr.execute(query)
        return self.crsr.fetchall()
    def query_col_names(self,query):
        self.crsr.execute(query)
        return [i[0].encode('utf8') for i in self.crsr.description]
    def __del__(self):
        self.db.close()
