import HTML
class CreateHTMLTable:
    def createHTML(self,table_data,monthname):
        htmlcode = '<b>' + monthname + '</b><br><br>'
        htmlcode += HTML.table(table_data)
        return htmlcode