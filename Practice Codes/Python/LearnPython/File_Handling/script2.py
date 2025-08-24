# To update a file
import os

if __name__ == '__main__':
    
    print("Updating the file: text1.txt\n")

    try:
        f1=open("text2.txt",'a')
        f1.write("\nLine number three is updated")
        f1.flush()
    finally:
        print("File Updated!")
        f1.close()