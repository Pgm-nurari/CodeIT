# To write into a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table1.csv",'w')
        csv_writer = csv.writer(file_handle)
        fields = ['SI No.','Full Name','Phone','Roll No']
        rows = [[1,'Akash',1234567089,101],[2,'Erick',2345678091,102],[3,'Suraj',3456789102,120]]
        
        csv_writer.writerow(fields) # Inserting the header row ( column names )...
        csv_writer.writerows(rows) # Inserting all the rows...
        
        file_handle.flush()
    
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    