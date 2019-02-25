import mysql.connector as m
db = m.connect(host="localhost", user="root", password="root", db="Student_monthly_report")
crsr=db.cursor()



