# test.py

import oracledb
import os

with oracledb.connect(user = 'system',host = 'localhost', port = 1521,service_name = 'xepdb1', password= '21cadmin') as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)