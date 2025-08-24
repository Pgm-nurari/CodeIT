import tkinter as tk

if __name__=='__main__':

    k="Hello this is buttons page!"
    print(k)
    print(k,file=open('readable.txt','a'))

    minsizeList=[1,1]
    new_list =  [minsizeList[i]>0 for i in range(len(minsizeList))]
    if new_list[0] and new_list[1]:
        print(f"Passed: {new_list}")
    else:
        print(f"Failed {new_list}")

       