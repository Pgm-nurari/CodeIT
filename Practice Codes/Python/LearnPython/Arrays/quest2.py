import os
from array import *

if __name__ == '__main__':
    '''
2.  Write a code to reverse an array without using 
    in-built functions?    
    '''

    arr = array('i',[1,2,3,4,5])
    new_arry = array('i',[])
    for i in range(len(arr)):
        new_arry =new_arry + array('i',[arr[-i-1]])
    
    print("arr: ",arr)
    print("new_array: ",new_arry)