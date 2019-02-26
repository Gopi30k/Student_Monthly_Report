import logging

class DBQuery_Extractor:
    # def __init__(self,fileName):
    #     self.fileName
    def fetch_Query(self,fileName):
        tlist = []
        query_strs = {}
        try:
            fd=open(fileName,'r')

            sqlFile = fd.read().replace('\n','')
            sqlcmds=sqlFile.split(';')
            sqlcmds.pop()
            return dict(i.split(':') for i in sqlcmds)
        except Exception:
            logging.info("Error: can\'t find SQL file or read data")




