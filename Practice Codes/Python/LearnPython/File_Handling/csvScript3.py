# To read from a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table1.csv",'r')
        csv_reader = csv.reader(file_handle)
        fields = next(csv_reader)
        
        for head_attr in fields:
            print(head_attr,end="\t")
        
        for row in csv_reader:
            
            for value in row:
                print(value,end="\t")
            print()
        
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    