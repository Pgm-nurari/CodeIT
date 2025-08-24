# To read from a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table2.csv",'r')
        csv_reader = csv.DictReader(file_handle)
        
        for i in list(csv_reader):
            print(csv_reader)
        
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
