import qrcode
import mysql.connector


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Maitri@2001",
        database="student_managment"
    )

mycursor = mydb.cursor()

def generateQR():
    name=input('Enter the name (Name Surname): ')
    age=input('Enter date of birth (dd/mm/yyyy): ')
    std=int(input('Enter te class: '))

    query="SELECT id FROM student ORDER BY id DESC LIMIT 1;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    sid=""
    if(myresult==[]):
        sid=sid+'001'
    else:
        idPreInt=0
        for i in myresult:
            idPre=i[0]
            idPreInt=idPreInt*10+int(idPre[0])
            idPreInt=idPreInt*10+int(idPre[1])
            idPreInt=idPreInt*10+int(idPre[2])
        idPreInt=idPreInt+1
        tempPreId=idPreInt
        count=0
        while(tempPreId!=0):
            count=count+1
            tempPreId=int(tempPreId/10)
        lst=[str(i) for i in str(idPreInt)]
        if(count==1):
            sid=sid+'0'+'0'+lst[0]
        elif(count==2):
            sid=sid+'0'+lst[0]+lst[1]
        else:
            sid=sid+lst[0]+lst[1]+lst[2]


    for i in name:
        if(ord(i)>=65 and ord(i)<=90):
            sid=sid+i

    sid=sid+age[6:]

    print(sid,name,age,std)  
    sql = "INSERT INTO Student (id,name,age,std) VALUES ('{}','{}','{}',{})".format(sid,name,age,std)
    mycursor.execute(sql)
    mydb.commit()

    print('Generating.....')
    img=qrcode.make(sid)
    img.save('E:\CODING\Project\QR code\QR\{}.jpg'.format(sid))
    print('QR generated')
    return


