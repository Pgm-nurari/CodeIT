# To read from a file
import os

if __name__ == '__main__':
    
    print("[--------------------------------]")
    print("Reading from the file: text1.txt")
    print("[--------------------------------]")
    
    try:
        f1 = open("text1.txt",'r')
        robj=f1.read()
        print(robj)
    #   print(f1.read())
    
    finally:
        f1.close()
        print("Success...")