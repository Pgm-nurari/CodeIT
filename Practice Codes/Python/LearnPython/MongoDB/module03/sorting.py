import pymongo
import pandas as pd

def main():
    con = pymongo.MongoClient("mongodb://localhost:27017/")
    
    tab1 = con['mydatabase']['customers']

    # for i in tab1.list_collection_names():
    #     print(i)

    ascending = tab1.find().sort('name',1)
    descending = tab1.find().sort('name',-1)
    
    print("\nPrinting data in ascending order:\n")
    for i in ascending:
        print(i)

    print("\n\nPrinting data in descending order:\n")
    for i in descending:
        print(i)

if __name__=='__main__':
    main()