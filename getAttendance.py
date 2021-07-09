from prettytable import PrettyTable
import mysql.connector
x = PrettyTable()

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Maitri@2001",
        database="student_managment"
    )

mycursor = mydb.cursor()

def getByEmpID():
    sid=input('Enter the id for which you want the attendance: ')
    query="SELECT * FROM attendance WHERE id='{}';".format(sid)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    x.field_names = ["ID", "DATE", "IN Time", "OUT Time"]
    for i in myresult:
        x.add_row(list(i))
    print(x.get_string(fields=["ID", "DATE","IN Time","OUT Time"]))
    return

def getByDate():
    date=input('Enter the date for which you want the attendance: ')
    query="SELECT * FROM attendance WHERE date='{}';".format(date)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    x.field_names = ["ID", "DATE", "IN Time", "OUT Time"]
    for i in myresult:
        x.add_row(list(i))
    print(x.get_string(fields=["ID", "DATE","IN Time","OUT Time"]))
    return

def getByDateAndEmpID():
    sid=input('Enter the id for which you want the attendance: ')
    date=input('Enter the date for which you want the attendance: ')
    query="SELECT * FROM attendance WHERE id='{}' and date='{}';".format(sid,date)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    x.field_names = ["ID", "DATE", "IN Time", "OUT Time"]
    for i in myresult:
        x.add_row(list(i))
    print(x.get_string(fields=["ID", "DATE","IN Time","OUT Time"]))
    return

def getAttendance():
    print('1: According to Employee ID')
    print('2: According to date')
    print('3: Accoring to date and Employee ID')
    choice=int(input('Your Choice: '))
    if(choice==1):
        getByEmpID()
        return
    elif(choice==2):
        getByDate()
        return
    elif(choice==3):
        getByDateAndEmpID()
        return


