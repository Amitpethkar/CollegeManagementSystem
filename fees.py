import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table fees( Name varchar(100), Class varchar(10), Roll_No varchar(10), Month_Year varchar(20), Fees varchar(10), Date varchar(20))")