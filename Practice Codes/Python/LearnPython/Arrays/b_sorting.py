from array import *

def show(arr):
    for a in arr:
        print(a,end=' ')    

def sort1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    show(arr)

def sort2(arr):
    pass
if __name__=='__main__':

    arr1 = array('i',[5,47,-9,6,-7,-45,15,0,474,-10])
    for i in range(len(arr1)):
        for j in range(i,len(arr1)-1):
            if arr1[i]>arr1[j+1]:
                temp=arr1[i]
                arr1[i]=arr1[j+1]
                arr1[j+1]=temp
    show(arr1)