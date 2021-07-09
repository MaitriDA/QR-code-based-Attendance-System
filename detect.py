import cv2;
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Maitri@2001",
        database="student_managment"
    )

mycursor = mydb.cursor()

def markAttendance(myData):
    now = datetime.now()
    sid=myData
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    
    query="SELECT * FROM attendance WHERE id='{}' and date='{}';".format(sid,date)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    in_time=''
    out_time=''
    for i in myresult:
        in_time=i[2]
        out_time=i[3]
    
    if(myresult==[]):
        query="INSERT INTO attendance  (id,date,in_time) value ('{}','{}','{}');".format(sid,date,time)
        mycursor.execute(query)
        mydb.commit()
        print('Attendance marked for in time')
    elif(in_time!=None and out_time==None):
        query="UPDATE attendance SET out_time='{}' WHERE id='{}' and date='{}';".format(time,sid,date)
        mycursor.execute(query)
        mydb.commit()
        print('Attendance marked for out time')
    else:
        print('Attendance already marked for today')

     


def detectQR():
    print('Detecting.....')
    cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3,640)
    cap.set(4,480)
    flag=0

    while (flag==0):
        success,img=cap.read()
        for code in decode(img):
            myData=code.data.decode('utf-8')
            pts=np.array([code.polygon],np.int32)
            pts=pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,0),5)
            

            query="SELECT id FROM student WHERE id='{}';".format(myData)
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            student=""
            for i in myresult:
                student=i[0]
            if(student==myData):
                markAttendance(myData)
                cv2.destroyAllWindows()
                return 1
            else:
                cv2.destroyAllWindows()
                return 0
        cv2.imshow('Result',img)
        if (cv2.waitKey(1)==27):
            cv2.destroyAllWindows()
            return
    return
