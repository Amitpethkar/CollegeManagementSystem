import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table tattendance( Date varchar(10), Absent_Teachers varchar(200))")