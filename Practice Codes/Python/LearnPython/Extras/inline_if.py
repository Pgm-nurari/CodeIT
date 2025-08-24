"""
In this file we will be learning about inline-if statements in Python languages.
They are an amazing way to write single statement if-else conditions.

Python provides two ways to write inline if statements. These are:
    1. if condition: statement
    2. s1 if condition else s2
"""

import os

if __name__=='__main__':
    os.system('cls')
    print(__doc__)
    
    print("....INLINE STATEMENTS....")
    print("Using method one: ")
    try:
        a=eval(input("Enter the boolean value"))
    except:
        print("Entre the boolean value properly")
    finally:
        if a: print("Hello World and its People")
    
    print("Using method two: ")
    try:
        a=eval(input("Enter the boolean value"))
    except:
        print("Entre the boolean value properly")
    finally:
        print("if statement" if a==True else "else statement")
    