"""_summary_: most useful when the value only changes, but the overall code remains same...

"""
import cx_Oracle as cx
from sys import exit

try :
    conn = cx.connect('system','21cadmin','localhost:1521/xepdb1')
except Exception as err:
    print('Connection Failed')
    print('Enter the Connection Credentials properly')
else:
    print('Connection Successful\n',conn.version)
    cur = conn.cursor()
    try: 
        var1 = int(input("Entre the age for the condition: "))
        query = """ select * from test_table where age >= :var1""" # var1 is the binding variable...
        cur.execute(query,{'var1': var1})                          # it should be in a dictionary...
        rows = cur.fetchall()
        
        for i in rows:
            print(i)
        
        
    except Exception as err:
        print("Could not fetch all the details...")
    else:
        print("Completed...")

finally:
    if input("Press Enter to exit: "):
        cur.close()
        conn.close()
        exit(0)
        