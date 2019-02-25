import re
import HTMLGenerator
import logging
import DBQueries as DBQ
import QueryExecution as Q
queryObj=DBQ.DBQuery_Extractor()
QueryDict={}
QueryDict=queryObj.fetch_Query('Student_monthly_report.sql')

identifierList=QueryDict.keys()
identifierList.sort()
TaskQueries=[]
for i in identifierList:
        if re.search("TASK",i):
            TaskQueries.append(i)
        else:
            Q.DBQueryExecution(QueryDict[i])

monthdict={
'January':"'%-01-%'",
'February':"'%-02-%'",
'March':"'%-03-%'",
'April':"'%-04-%'",
'May':"'%-05-%'",
'June':"'%-06-%'",
'July':"'%-07-%'",
'August':"'%-08-%'",
'September':"'%-09-%'",
'October':"'%-10-%'",
'November':"'%-11-%'",
'December':"'%-12-%'"

}

res1=Q.SELECTQueryExe(QueryDict['31_TASK_EXE_1'])
decoding=[i[0] for i in res1]
monthList=[i.encode('utf8') for i in decoding]
print monthList


res=[]
code=''
htmlObg=HTMLGenerator.CreateHTML('Student_monthly_report.html')
for i in monthList:
    res=(Q.SELECTQueryExe1(QueryDict['32_TASK_EXE_2'],monthdict[i]))
    code+=htmlObg.createHTMLtable(res,i)
htmlObg.writeToFile(code)
