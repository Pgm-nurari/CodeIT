# Practicing Date Class in python using the datetime module...
from datetime import date,datetime
import os
#Format of date is: yyyy-mm-dd
def ex_01():
    word='''It accepts arguments based on reallife, for example: Entering 29th as day for a 
    non-leap year february: (2015,2,29) will give you ValueError...
    But when you pass a 29th february of a leap error it does not give any error.
    Siimilarly correct dates must be entered for all dates.'''
    print(word)
    x=int(input("Enter [1] for initializing  a date variable: "))
    if(x==1):
        os.system("clear")
        print("Enter the details in numerical values...")
        year=int(input("Year: "))
        month=int(input("Month: "))
        day=int(input("Day: "))
        print("The date you entered is: ",date(year,month,day))
    else: os.system('clear')

def ex_02():
    print("To get current date, using today() function.")
    today=date.today()
    print("\nToday's date is: ",today)
    print("\nCurrent Year is: ",today.year)
    mon_list={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
              7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    month=today.month
    print("Current Month is: ",mon_list[month])
    print("Current Day is: ",today.day)

def ex_03():
    print("Getting the time and date frrom timestamp.")
    date_time=datetime.fromtimestamp(20000)
    #The parameter entered is the seconds from 1st Jan 1970...
    print("Date using timestamp is: ",date_time)

def ex_04():
    print("Converting date to string.")
    today=date.today()
    Str=date.isoformat(today)
    print("String Representation",Str)
    print(type(Str))

if __name__=='__main__':
    os.system('clear')
    '''
    x=0
    while(x==0):
        ex_04()
        x=int(input("Enter [0] to Continue: "))
    else: 
        os.system('clear')
    '''
    print("Refer to the file(datetime.txt) first for info on Date class:")
    myfile=open("//home/mrpgm/Documents/sabhyam/Python/datetime.txt",'r')
    print(myfile.read())