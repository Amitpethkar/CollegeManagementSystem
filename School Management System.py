import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXXXX")
mycursor= mydb.cursor()

mycursor.execute("Create database schoolManagementSystemDB")