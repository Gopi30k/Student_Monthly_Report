import LogGen as log
class FILE_handling:

    def readFromFile(self,file_name):
        MFile=open(file_name,'r')
        return MFile.read().replace('\n','')
    def writeToFile(self,file_name,values):
        MFile= open(file_name,'w')
        MFile.write(values)

class Query_Extractor(FILE_handling):
    def list_Of_SQL_cmds(self,QueryFile):
        try:
            cmds=FILE_handling().readFromFile(QueryFile).split(';')
        except Exception:
            log.logger.error("Query File %s reading Err",QueryFile)
        else:
            log.logger.info("Query File %s read successfully",QueryFile)
        cmds.pop()
        return cmds