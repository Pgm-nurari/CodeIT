import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def checkConnectionFirst(host_name="loca", port_num=27017):
    try:
        c = MongoClient(host=host_name, port=port_num)
        print("Connection Made Successfully!!")
        return c
    except ConnectionFailure as e:
        sys.stderr.write(f'Could not connect to MongoDB: {e}\n')
        return None

def checkConnectionSecond(host_name="localhost", port_num=27017):
    try:
        c = MongoClient(host=host_name, port=port_num)
        c.admin.command("ping")
        print("Connection Made Successfully!!")
        return c
    except ConnectionFailure as e:
        sys.stderr.write(f'Could not connect to MongoDB: {e}\n')
        return e

def main():
    # con = checkConnectionFirst()
    con = checkConnectionSecond(host_name="localhost")
    print(con.list_database_names())

if __name__ == '__main__':
    main()