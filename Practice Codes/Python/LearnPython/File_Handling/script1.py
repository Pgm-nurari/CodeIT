# Opening and closing a file
'''
There are two types of files:
    1. ByDefault 't' or 'text' type
    2. 'b' or 'binary format'
Files can be accessed in 4 ways:
    1. 'w' --> write mode
    2. 'r' --> read mode
    3. '+' --> read or write both mode
    4. 'a' --> append mode
'''
import os

if __name__=='__main__':
    
    f1 = open("text1.txt",'w')
    f1.write("Hello World...\nThis is the first example of writing into a file and closing it.")
    f1.flush()
    f1.close()
    print("File created\n")      
    os.system('exit')
    