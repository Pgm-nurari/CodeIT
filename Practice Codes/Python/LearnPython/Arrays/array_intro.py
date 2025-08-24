import math,os
from array import *



def int_arr1():
    arr1 = array('i',[1,2,-3,4,5])
    print("Address and Size of array :",arr1.buffer_info())

    print("After reversing the array: ",end='')
    arr1.reverse()
    print(arr1)
    arr1.reverse()

    print("printing the values one-by-one")
    for i in arr1: 
        print(i)    

    new_arr = array(arr1.typecode,[a for a in arr1])
    print("New copied array is: ",new_arr)

def char_arr2():
    arr2 = array('u',['a','b','c','d','e'])
    print("Address and Size of array :",arr2.buffer_info())

    print("After reversing the array: ",end='')
    arr2.reverse()
    print(arr2)
    arr2.reverse()

    print("printing the values one-by-one")
    for i in arr2: 
        print(i)            

if __name__=='__main__':
    #os.system('cls')

    ch=int(input("Choose  any one:\n1. Int Array\n2. Char Array\n"))
    match (ch):
        case 1: 
            os.system('cls')
            int_arr1(); 
        case 2: 
            os.system('cls')
            char_arr2(); 
        case _: print("Invalid Selection...")