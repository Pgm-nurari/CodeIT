# Other methods for File Handling in python

'''
There are 4 read methods:
    1. read(n) => Reads characters from 1 to 'n' counts.
    2. readline(n) => Reads 'n' lines of data.
    3. readlines() => Returns all the lines as an element of a list
    4. read()
There are 2 write methods:
    1. write() => Already covered.
    2. writelines(<iterable : string_type>) => Insert all lines as a list.
There are 2 other methods namely:
    1. tell() => Returns the position of pointer as an integer.
    2. seek(n,s) => Places the pointer at 's' and seeks upto next 'n' counts from there.
'''

import os

if __name__=='__main__':
    
    try:
        f2 = open("text2.txt",'r')
        f3 = open("text3.txt",'w')
        while(True) :
            dict1 = { 1: "f.read(n)", 2: "f.readline(n)", 3: "f.readlines()", 4: "f.writelines(list)"}
            for i in dict1:
                print(i,dict1[i],sep=" :")
            ch = int(input("Select your choice: "))
            
            match(ch):
                case 1:
                    print(ch,dict1[ch],"\n")
                    robj = f2.read(int(input("Enter number of characters :")))
                    print("Output:\n",robj)
                    continue
                case 2:
                    print(ch,dict1[ch],"\n")
                    print(" Printing first 10 characters from each line: \n")
                    size = len(f2.readlines())
                    f2.seek(0)
                    for i in range(size):
                        print(f2.readline().rstrip("\n"))
                    continue
                case 3:
                    print(ch,dict1[ch],"\n")
                    robj = f2.readlines()
                    print("Output: \n",robj)
                    continue
                case 4:
                    print(ch,dict1[ch],"\n")
                    n = int(input("Enter the number of lines: "))
                    Lines=[]
                    for i in range(n):
                        Lines.append(input(f"Enter: {i+1}\n")+"\n")
                    f3.writelines(Lines)
                    f3.flush()
                    print("Entred !")
                    continue
                case _:
                    print("Invalid option")
                    os.system('exit')
                    break
            if (input("Do you want to continue")).lower()!='y':
                break
            
    finally:
        f2.close()
        f3.close()
        print("Done...!")