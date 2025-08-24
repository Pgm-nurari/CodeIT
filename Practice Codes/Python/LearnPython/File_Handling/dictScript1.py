# To write a dictionary list into a csv file...

import csv

if __name__ == '__main__':
    
    try:
        file_handle = open("table2.csv",'w')
        csv_writer = csv.DictWriter(file_handle,fieldnames = ['SI No.','Full Name','Phone','Roll No'])
        rows = [ 
                {'SI No.': 1, 'Full Name': 'Akash', 'Phone': 1234567089, 'Roll No': 101 }, 
                {'SI No.': 2, 'Full Name': 'Erick', 'Phone': 2345678091, 'Roll No': 102}, 
                {'SI No.': 3, 'Full Name': 'Suraj', 'Phone': 3456789102, 'Roll No': 120}
               ]
        
        csv_writer.writeheader() # Inserting the header row ( column names )...
        csv_writer.writerows(rows) # Inserting all the rows...
        
        file_handle.flush()
    
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    