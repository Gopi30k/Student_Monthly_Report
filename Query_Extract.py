import Queries_FileHandling as H_GA
class Query_To_List:
    def getQuery_as_List(self,SqlFileName):
        return H_GA.Query_Extractor().list_Of_SQL_cmds(SqlFileName)
