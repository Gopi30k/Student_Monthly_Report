import logging
import mysql.connector as MySQL
import base64 as b
import getpass
#pwd=raw_input("Enter password for database:")
# p=getpass.getpass(prompt="Pwd  ")


class DB_Connection:
    __pwd = 'cm9vdA=='
    def __init__(self):

        #enc=b.b64encode(pwd)
        self.db=MySQL.connect(host="localhost", user="root", password=b.b64decode(self.__pwd), db="Student_monthly_report_v2")
        self.crsr = self.db.cursor()
    def query(self,query):
        self.crsr.execute(query)
        return self.crsr.fetchall()
    def query_col_names(self,query):
        self.crsr.execute(query)
        return [i[0].encode('utf8') for i in self.crsr.description]
    def __del__(self):
        self.db.close()
