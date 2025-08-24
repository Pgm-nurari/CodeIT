# To update into a csv file...

import csv
import os

if __name__ == '__main__':
    
    try:
        file_handle = open("table1.csv",'a')
        csv_writer = csv.writer(file_handle)
        
        rows = [[4,'Kiran',4567089478,112],[5,'Nanu',1324678091,125],[6,'Gopi',2581749102,126]]
        
        csv_writer.writerows(rows) # Inserting all the rows...
        
        file_handle.flush()
    
    except:    
        raise SyntaxError
    finally:
        file_handle.close()
        print("Success!!!!")
    