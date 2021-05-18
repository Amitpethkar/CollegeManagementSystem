import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXX", database="schoolManagementSystemDB")
mycursor= mydb.cursor()
mycursor.execute("Create table salary( Name varchar(20), Month varchar(10), Yes_No varchar(5))")