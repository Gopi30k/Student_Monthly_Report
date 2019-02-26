import HTML
class CreateHTML:
    def __init__(self,fileName):
        self.HTMLfileName=fileName
        self.f=open(self.HTMLfileName,'w')
    def createHTMLtable(self,table_data,monthname):
        htmlcode = '<b>' + monthname + '</b><br><br>'
        htmlcode += HTML.table(table_data)
        return htmlcode
    def writeToFile(self,codeTowrite):
        self.f.write(codeTowrite)

