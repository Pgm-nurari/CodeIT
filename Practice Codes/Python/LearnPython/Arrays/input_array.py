from array import *
import os

def cntnu():
    ch=input("Do you want to continue: ")
    if ch.lower()=='y':
        os.system('cls')
    else:
        os.system('exit(0)')

if __name__=='__main__':

    # Declaring  an array...
    arr = array('i',[])
    length=int(input("Enter the number of your Array: "))
    for i in range(length):
        arr.append(int(input("Enter a value: ")))

    print("The Array is: ")
    for val in arr:
        print(val,end=' ') 
    
    cntnu()

    # Printing the index of the value in the array...
    num = int(input("Enter the number to Search its Index: "))
    k,flag = 0,0
    print("\n Method 01 ")
    for val in arr:
        if val == num: 
            flag = 1
            break
        else:
            flag = 0
        k+=1
    if flag == 1:
        print(k)
    else:
        print("Value_not_found...")
    
    print("\n Method 02 ")
    print(f"Index of {num} is: ",arr.index(num))




