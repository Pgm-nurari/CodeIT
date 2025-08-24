from module00.connection import checkConnectionSecond as m0c
from pymongo import collection
import pandas as pd

def singleData(table : collection):
    print(table.find_one())
    # print(tab1.count_documents(filter=1))

def multipleData(table : collection):
    for x in table.find():
        print(x)
    df = pd.DataFrame(table.find())
    print(df)
    print(df.describe())

def specificAttributes(table : collection):
    for x in table.find({},{ "_id": 0, "id": 1, "name": 1, "email": 1 }):
        print(x)
    # Excluding attributes like _id

    """
        You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
        If you specify a field with the value 0, all other fields get the value 1, and vice versa, put 'flag' as '0'
    """

    flag=0
    if flag!=0:
        for x in table.find({},{ "name": 1, "address": 0 }):
            print(x)
    

def main():
    
    tab1 = m0c()['mydatabase']['students']
    # singleData(table=tab1)
    # multipleData(table=tab1)
    specificAttributes(table=tab1)

if __name__=='__main__':
    main()