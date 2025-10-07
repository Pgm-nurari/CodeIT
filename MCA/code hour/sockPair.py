def countSockPairs(arr : list) -> int: 
    n = len(arr)
    uniques = list(set(arr))
    count = 0
    for i in uniques:
        count+= (arr.count(i)//2)
    return count

def main():
    socks = [10,20,30,20,45,55,10,35,35,20,10,10]
    print(f"Total no. of socks' pairs is: {countSockPairs(socks)}")

if __name__=='__main__':
    main()