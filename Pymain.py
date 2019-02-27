import Queries_FileHandling as H_GA
import Query_Extract as QE
import DataFrame_converter as DC
import Month_DF as MD


queryObj=QE.Query_To_List()
sql_cmds=queryObj.getQuery_as_List('Queries.sql')

dataFrameObj=MD.SQLToDataFrames()
list_of_DFS= dataFrameObj.createDF(sql_cmds)
htmlcode=""
for i in range(1,13):
    htmlcode+=DC.Dataframe_converter().Df_to_list(list_of_DFS[0],i)

FileWriteObj=H_GA.FILE_handling()
FileWriteObj.writeToFile("out.html",htmlcode)


