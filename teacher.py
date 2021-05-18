import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table teacher( Name varchar(100), Post varchar(200), Salary varchar(20), Address varchar(200), Phone varchar(20), Account_No varchar(50))")