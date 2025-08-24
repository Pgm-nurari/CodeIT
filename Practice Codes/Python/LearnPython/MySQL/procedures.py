import cx_Oracle as cx

try:
    conn = cx.connect('system','21cadmin','localhost:1521/xepdb1')
except:
    print("Connection failed to establish")
else:
    print("Connection Successful: ",conn.version)
    try:
        cur = conn.cursor()
        cur.callproc('dat',('Suraj','Rajesh','Lenovo',45))
    except:
        print("Procedure could not be called")
    else:
        cur.close()
    
finally: 
    conn.close()
    