# To update dictionary into a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table2.csv",'a')
        csv_writer = csv.DictWriter(file_handle,fieldnames = ['SI No.','Full Name','Phone','Roll No'])
        
        rows = [
                {'SI No.': 4, 'Full Name': 'Kiran', 'Phone': 4567089478, 'Roll No': 112 },
                {'SI No.': 5, 'Full Name': 'Nanu', 'Phone': 1324678091, 'Roll No': 125 },
                {'SI No.': 6, 'Full Name': 'Gopi', 'Phone': 2581749102, 'Roll No': 126 },
              ]
        
        csv_writer.writerows(rows) # Inserting all the rows...
        
        file_handle.flush()
    
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    