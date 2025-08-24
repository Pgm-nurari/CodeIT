# To read from a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table2.csv",'r')
        csv_reader = csv.DictReader(file_handle)
        
        print(list(csv_reader))
        """for i in csv_reader:
            print(list(csv_reader))"""
        
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    