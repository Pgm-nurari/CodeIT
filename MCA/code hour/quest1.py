#smallest number in an array
def smallestNum(arr):
    print(min(arr))

#frequency of each element in an array
def countElementsSorted(arr:list):
    unique = set(arr)
    c_dict = dict()
    print(c_dict)
    for i in unique:
        c_dict[i] = 0
    for i in arr:
        if i in unique:
            c_dict[i]+=1
    print(c_dict)
    return c_dict

def countElementsUnsorted(arr:list):
    unique = set(arr)
    c_dict = dict()
    print(c_dict)
    for i in arr:
        if i in unique:
            c_dict[i]=arr.count(i)
    print(c_dict)   
    return c_dict

# find the second smallest and largest in an array
def secondSmallBig(arr:list):
    arr.sort()
    print(f'Second smallest in array is: {arr[1]}\nSecond largest in array is: {arr[-2]}')
    return {'secondSmall': arr[1], 'secondBig':arr[-2]}

#sum of elements in an array
def sumArrayValues(arr: list):
    print(sum(arr))

#remove duplicate elements from an unsorted array
def uniqueElements(arr: list):
    print(list(set(arr)))

# search an element in an array:
def searchElement(arr:list, key):
    print(arr.index(key))

#check if a number is amstrong or not?
def amstrongCheck(num:int):
    new_num = 0
    p = len(str(num))
    temp = num
    while temp>0:
        x = temp%10
        new_num = x**p + new_num
        temp = temp//10
    if new_num==num:
        print(f"{num} is an amstrong number.")
    else:
        print(f"{num} is not an amstrong number.")

def main():
    countElementsUnsorted([1,2,4,4,3,4,2,3,4,4,4,44])

if __name__=='__main__':
    main()