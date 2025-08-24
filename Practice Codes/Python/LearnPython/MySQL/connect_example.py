import cx_Oracle as cx


try :
    # Create Connection
    conn = cx.connect('system/21cadmin@//localhost:1521/xepdb1')
except Exception as err:
    print("Error while creating the connection")
else :
    print(conn.version)
    try:
        # Create cursor
        cur = conn.cursor()
        sql_create = """
        create table test_table ( first_name varchar(50), last_name varchar(50), company varchar(50), age number(3))
        """
    except:
        print("Table not created!")
    else:
        cur.execute(sql_create)
        print("Table created!!")
        
finally:
    cur.close() 
    conn.close()