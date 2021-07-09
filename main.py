from datetime import datetime
import generate
import detect
import getAttendance

if __name__=='__main__':
    print('Hello')
    print('1: Mark Attendance')
    print('2: Add new Employee')
    print('3: Get Attendance')
    choice=int(input('Your choice: '))
    if(choice==1):
        res=detect.detectQR()
        if(res==0):
            print('Un Authorized')
            print('Please register first')
    elif(choice==2):
        generate.generateQR()
    elif(choice==3):
        getAttendance.getAttendance()
    else:
        print('Enter a valid choice')
    
