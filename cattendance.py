import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table cattendance( Date varchar(10), Class varchar(10), Absent_Students varchar(200))")