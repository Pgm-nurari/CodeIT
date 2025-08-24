from module00.connection import checkConnectionSecond as m0c

def insertOne(data: dict):
    con = m0c(host_name="localhost",port_num=27017)
    if con!=None:
        mydb = con["mydatabase"]
        tab01 = mydb["students"]
        i=tab01.insert_one(data)
        print(f'Fetching the id of data : {data}\nId : {i.inserted_id}')
    else:
        return con
    
def main():
    data=dict()
    print("Enter the data in following format: \nId\tname\temail\n")
    data['id']=int(input())
    data['name'] = input()
    data['email'] = input()

    print("Entering into the database......")
    insertOne(data=data)

if __name__=='__main__':
    main()