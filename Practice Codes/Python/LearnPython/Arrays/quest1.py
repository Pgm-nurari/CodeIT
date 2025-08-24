import os
from array import *

if __name__=='__main__':
    '''
1.  Create an array with 5 values and delete 
    the values at index 2 without using in-built functions?    
    '''
    arr=array('i',[1,2,3,4,5])
    new_arr=array(arr.typecode,[val for val in arr if (val!=arr[2])])
    print(arr,new_arr,end="\n")
