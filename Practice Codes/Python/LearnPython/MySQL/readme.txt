[...Python Modules...]
1. cx_oracle (Oracle database)
2. pyodbc (Microsoft SQL Server)
3. pymysql (MySQL)
4. Psycopg2 (PostgerSQL)

[...Steps to Communicate with database...]
1.  import the module of the specific database
2.  Establish connection: 
    > conn = cx_oracle.connect(database connection string)
    Eg: conn = cx-cx_oracle.connect('scott/tiger@localhost:port/service_name')
3.  Create Cursor:
    > cur = conn.cursor() // Used to execute the commands

[...Execute Query Methods...]
1.  cursor.execute() //To execute one Query
2.  cursor.executemany() //To execute many times (as parameters..)

[...Fetching Data Methods...]
1.  cursor.fetch()      //To fetch one row
2.  cursor.fetchall()   //To fetch all the rows
3.  cursor.fetchmany(n) //To fetch n rows

[...Commit or Rollback...]
1.  cursor.commit()
2.  cursor.rollback()

[...Closing...]
1.  cursor.close()
2.  connection.close()