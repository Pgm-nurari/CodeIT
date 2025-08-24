"""_summary_
                There are 3 methods to fetch data:  (i) fetchone() => fetch 1 row at a time.
                                                    (ii) fetchall() => fetch all the the rows at a time.
                                                    (iii) fetchmany(n) => fetch 'n' no. of rows at a time.
"""

import cx_Oracle as cx
import sys

try :
    conn = cx.connect('system','21cadmin','localhost:1521/xepdb1')
except Exception as err:
    print('Connection Failed')
    print('Enter the Connection Credentials properly')
else:
    print('Connection Successful\n',conn.version)
    cur = conn.cursor()
    try: 
        query = """ select * from test_table"""
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as err:
        print("Could not fetch all the details...")
    else:
        print("Fetching all the data at once with row number: ")
        for index,row in enumerate(rows):
            print(index, row, sep = " ")
    

finally:
    if input("Press Enter to exit: "):
        cur.close()
        conn.close()
        sys.exit(0)