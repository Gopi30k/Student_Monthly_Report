import DataAccess as DA
import pandas as pd
import Queries_FileHandling as H_GA
import DataAccess as DA
import datetime
DBobj=DA.DB_Connection()
DB_sql_cmds=H_GA.Query_Extractor().list_Of_SQL_cmds('Queries.sql')


Db_Data=[]
Db_Colnames=[]
for db_query in DB_sql_cmds:
    Db_Data.append(DA.DB_Connection().query(db_query))
    Db_Colnames.append(DA.DB_Connection().query_col_names(db_query))

Db_Sql_Tables=[]
for itr in range(0,len(Db_Data)):
    Db_Sql_Tables.append(pd.DataFrame(Db_Data[itr],columns=Db_Colnames[itr]))

# Total=0
# for index,row in Db_Sql_Tables[0].iterrows():


Db_Sql_Tables[0]['Total']=Db_Sql_Tables[0]['English']+Db_Sql_Tables[0]['Tamil']+Db_Sql_Tables[0]['Maths']+Db_Sql_Tables[0]['Science']+Db_Sql_Tables[0]['Social']


# Db_Sql_Tables[0]['Rank']=Db_Sql_Tables[0]['Total'].rank()
# Db_Sql_Tables[0].sort_values("Total",ascending=False,inplace = True)
# print Db_Sql_Tables[0]

Db_Sql_Tables[0].sort_values("Total",ascending=False,inplace = True)
Db_Sql_Tables[0].insert(len(Db_Sql_Tables[0].columns),'Rank',range(1,1+len(Db_Sql_Tables[0])))
#Db_Sql_Tables[0].groupby(Db_Sql_Tables[0].examDate.dt.year)

# print Db_Sql_Tables[0].dtypes
# Db_Sql_Tables[0]['examDate']= Db_Sql_Tables[0]['examDate'].astype(str)
# print Db_Sql_Tables[0].dtypes

#s1 = "%-02-%"
# Db_Sql_Tables[0]['examDate']
# for index,row in Db_Sql_Tables[0].iterrows():
#     if s1 in Db_Sql_Tables[0]['examDate']:
#         print Db_Sql_Tables[0]['examDate']
#     else:
#         print Db_Sql_Tables[0]['examDate']

# Db_Sql_Tables[0].examDate=Db_Sql_Tables[0].examDate.str.slice(4,7)
# print Db_Sql_Tables[0]
# Db_Sql_Tables[0]['examDate'] = pd.to_datetime(Db_Sql_Tables[0]['examDate'])
# start_date = '2018-01-01'
# end_date = '2018-03-22'

# mask = (Db_Sql_Tables[0]['examDate'] > start_date) & (Db_Sql_Tables[0]['examDate'] <= end_date)
# print mask
# Db_Sql_Tables[0] = Db_Sql_Tables[0].loc[mask]
# print Db_Sql_Tables[0]

# print Db_Sql_Tables[0][Db_Sql_Tables[0].examDate.str.match(r'^2018-01')]

TempDF=Db_Sql_Tables[0][ pd.DatetimeIndex(Db_Sql_Tables[0]['examDate']).month==1]
print TempDF

TempDF.to_html("one.html")

for i in range(1,13):
    month_Df=dataFrameObj.monthDF(list_of_DFS[0],i)
    header=list(month_Df.columns.values)
    row_data=month_Df.values.tolist()
    row_data.insert(0,header)
    htmcode+=H.CreateHTMLTable().createHTML(row_data,calendar.month_name[i])



H_GA.FILE_handling().writeToFile("out.html",htmcode)
