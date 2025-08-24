import pymongo
import pandas as pd
from pymongo.errors import CollectionInvalid 

def del1(mycol):
    myquery = { "address": "Mountain 21" }
    mycol.delete_one(myquery)

def del2(mycol):
    myquery = { "address": {"$regex": "^S"} }
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

def del3(mycol):
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")

def del4(con : pymongo.MongoClient):
    print("\nProvided are collections before deletion:")
    for i in con['mydatabase'].list_collection_names():
        print(i)
    
    print("\nProvided are collections after deletion: ")
    try:
        X = con["mydatabase"].drop_collection('customers')
        print("Deleted collection is ",X)
    except CollectionInvalid as e:
        print(e)

def main():
    con = pymongo.MongoClient("mongodb://localhost:27017/")
    
    tab1 = con['mydatabase']['customers']

    del4(con)

if __name__=='__main__':
    main()