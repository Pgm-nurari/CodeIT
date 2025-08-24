import cx_Oracle as cx

try:
    conn = cx.connect("system","21cadmin","localhost:1521/xepdb1")
except Exception as Err:
    print("Connection failed, retry with correct and proper Credentials!")
else:
    print("Connection Successful")
    print(f"The connection version is: {conn.version}")
    try:
        cur = conn.cursor()
        sql_insert = """insert into test_table values(:1, :2, :3, :4) """ # Binding in execute() method
        data = [('Sundar','Pichai','Google',40), ('Mark','Zuckerburg','Facebook',57)]
        cur.executemany(sql_insert, data)
    except Exception as err:
        print("Error: ",err)
    else:
        print("Data inserted")
        conn.commit()    
        
finally:
    pass