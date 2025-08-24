import math,os
from array import *

# Matrix Addition...

def int_arr1():
    arr1 = array('i',[1,2,-3,4,5])
    print("Address and Size of array :",arr1.buffer_info())

    new_arr = array(arr1.typecode,[a for a in arr1])
    print("New copied array is: ",new_arr)

    return arr1
     

if __name__=='__main__':
    #os.system('cls')

    arr1 = int_arr1()
    
    i=0
    while i<len(arr1):
        print(arr1[i])
        i+=1

