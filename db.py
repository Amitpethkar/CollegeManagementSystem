import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="XXXX", database="schoolManagementSystemDB")


def ast():

    n = input("Student Name :")

    c = input("Class Name : ")

    r = input("Roll No : ")

    a = input("Address : ")

    p = input("Phone : ")

    data = [n,c,r,a,p]

    sql = 'insert into student values(%s,%s,%s,%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Entered Successfully")

    print(">——————————————————————————————————–<")

    main()

def rst():

    c = input("Class Name : ")

    r = input("Roll No : ")

    data = (c,r)

    sql = 'delete from student where Class = %s and Roll_No = %s'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Updated")

    print(">——————————————————————————————————–<")

    main()

def addt():

    n = input("Teacher : ")

    p = input("Post : ")

    s = input("Salary : ")

    a = input("Address : ")

    ph = input("Phone : ")

    ac = input("Account : ")

    data = [n,p,s,a,ph,ac]

    sql = 'insert into teacher values(%s,%s,%s,%s,%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Entered Successfully")

    print(">——————————————————————————————————–<")

    main()

def remt():

    n = input("Teacher Name : ")

    ac = input("Account No : ")

    data = (n,ac)

    sql = 'delete from teacher where Name = %s and Account_No = %s'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Updated")

    print(">——————————————————————————————————–<")

    main()

def abclass():

    d = input("Date : ")

    cl = input("Class : ")

    ab = input("Names of Absent Students : ")

    data = [d,cl,ab]

    sql = 'insert into cattendance values(%s,%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Updated")

    print(">——————————————————————————————————–<")

    main()

def abteacher():

    d = input("Date : ")

    ab = input("Names of Absent Teacher : ")

    data = [d,ab]

    sql = 'insert into tattendance values(%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Updated")

    print(">——————————————————————————————————–<")

    main()

def submitf():

    n = input("Student Name : ")

    c = input("Class Name : ")

    r = input("Roll No : ")

    m = input("Month and Year : ")

    f = input("Fees : ")

    d = input("Date : ")

    data = [n,c,r,m,f,d]

    sql = 'insert into fees values(%s,%s,%s,%s,%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Entered Successfully")

    print(">——————————————————————————————————–<")

    main()

def pays():

    n = input("Teacher Name : ")

    m = input("Month : ")

    p = input("Yes / No : ")

    data = [n,m,p]

    sql = 'insert into salary values(%s,%s,%s)'

    c = mydb.cursor()

    c.execute(sql,data)

    mydb.commit()

    print("Data Entered Successfully")

    print(">——————————————————————————————————–<")

    main()

def dclass():

    cl = input("Class : ")

    data = [cl,]

    sql = 'select * from student where Class = %s'

    c = mydb.cursor()

    c.execute(sql,data)

    d = c.fetchall()           # [(6,6,5,6,8),(6,5,6,5,1),(5,4,7,6)]

    for i in d:

        print("NAME : ",i[0])

        print("CLASS : ",i[1])

        print("ROLL : ",i[2])

        print("ADDRESS : ",i[3])

        print("PHONE : ",i[4])

        print(">————————————–<")

    print(">——————————————————————————————————–<")

    main()

def dteacher():

    sql = 'select * from teacher'

    c = mydb.cursor()

    c.execute(sql)

    d = c.fetchall()

    for i in d:

        print("NAME : ",i[0])

        print("POST : ",i[1])

        print("SALARY : ",i[2])

        print("ADDRESS : ",i[3])

        print("PHONE : ",i[4])

        print("ACNO : ",i[5])

        print(">————————————–<")

    print(">——————————————————————————————————–<")

    main()

def viewAbSt():
    sql= 'select Absent_Students from cattendance'
    c= mydb.cursor()
    c.execute(sql)
    d= c.fetchall()

    for i in d:
        print("NAME: ", i[0])
        print(">————————————–<")

    print(">——————————————————————————————————–<")

    main()


def viewAbT():
    sql = 'select Absent_Teachers from tattendance'
    c = mydb.cursor()
    c.execute(sql)
    d = c.fetchall()

    for i in d:
        print("NAME: ", i[0])
        print(">————————————–<")

    print(">——————————————————————————————————–<")

    main()

def main():

    print("""                                   VIIT COMP DEPARTMENT

                            1.  ADD STUDENT                     2.  REMOVE STUDENT

                            3.  ADD TEACHER                     4.  REMOVE TEACHER

                            5. CLASS ATTENDANCE                 6.  TEACHER ATTENDANCE

                            7. SUBMIT FEES                      8.  PAY SALARY

                            9. DISPLAY CLASS                    10. TEACHERS LIST
                            
                            11. VIEW ABSENT STUDENTS            12. VIEW ABSENT TEACHERS

""" )

    choice = input("Enter Task No : ")

    print(">————————————–<")

    if (choice == '1'):

        ast()

    elif (choice=='2'):

        rst()

    elif (choice=='3'):

       addt()

    elif (choice=='4'):

        remt()

    elif (choice=='5'):

        abclass()

    elif (choice == '6'):

        abteacher()

    elif (choice=='7'):

        submitf()

    elif (choice == '8'):

        pays()

    elif (choice == '9'):

        dclass()

    elif (choice == '10'):

        dteacher()

    elif (choice == '11'):

        viewAbSt()

    elif (choice == '12'):

        viewAbT()

    else:

        print(" Wrong choice ")

        main()

def pswd():

    p = input("Password : ")

    if p == "VIIT":

        main()

    else:

        print("Wrong Password  ")

        pswd()

pswd()