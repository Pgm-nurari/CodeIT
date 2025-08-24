from module00.connection import checkConnectionSecond as m0c

def insertMany(data: list):
    con = m0c(host_name="localhost",port_num=27017)
    if con!=None:
        mydb = con["mydatabase"]
        tab01 = mydb["students"]
        i=tab01.insert_many(data)
        print(f'Fetching the id of data : {data}\nId : {i.inserted_ids}')
    else:
        return con
    
def main():
    entries = []
    print("Enter 3 data in the following format, separated by spaces: \nId\tname\temail\n")
    for i in range(3):
        data=dict()
        entry = input().split()
        if entry[0].isnumeric():
            data['_id'] = int(entry[0])
            data['name'] = entry[1]
            data['email'] = entry[2]
            entries.append(data)
        else:
            i-=1
            print(f"id : must be an integer...!")
            continue
    print(entries)
    print("Entering into the database......")
    insertMany(data=entries)

if __name__=='__main__':
    main()