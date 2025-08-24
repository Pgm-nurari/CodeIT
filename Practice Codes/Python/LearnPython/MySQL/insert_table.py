import cx_Oracle as cx


try :
    # Create Connection
    conn = cx.connect('system/21cadmin@//localhost:1521/xepdb1')
except Exception as err:
    print("Error while creating the connection")
else :
    print("Connection Successful\n")
    try:
        # Create cursor
        cur = conn.cursor()
        sql_insert = """insert into test_table values('Sabhyam','Mishra','Glider Inc',100) """
        cur.execute(sql_insert)
    except Exception as err:
        print("Error: ",err)
    else:
        print("Data inserted")
        conn.commit()
finally:
    cur.close()
    conn.close()
