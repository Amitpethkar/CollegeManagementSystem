import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table student(Name varchar(200), Class varchar(20), Roll_No varchar(50), Address varchar(500), Phone_No varchar(50))")