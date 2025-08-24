import pymongo

def update01(mycol : pymongo.collection):
    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }
    mycol.update_one(myquery, newvalues)

def update02(mycol : pymongo.collection):
    myquery = { "address": { "$regex": "^S" } }
    newvalues = { "$set": { "name": "Minnie" } }
    x = mycol.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    update02(mycol=mycol)

    #print "customers" after the update:
    for x in mycol.find():
        print(x)    

if __name__=='__main__':
    main()