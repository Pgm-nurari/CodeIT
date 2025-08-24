import cx_Oracle as cx

try:
    credentials = input("Enter the user_name, password, host, port, service_name: \n").split()
    hostPortSC = credentials[2] + ':' + credentials[3] + '/' + credentials[4]
    conn = cx.connect(credentials[0], credentials[1], hostPortSC)
except:
    print("Connection could not be established")
    print("Enter the credentials properly")
else:
    print(conn.version)
finally:
    conn.close()
