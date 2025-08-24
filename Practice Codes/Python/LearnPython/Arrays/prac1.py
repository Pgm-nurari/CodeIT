from array import *

def show(arr):
    for a in arr:
        print(a,end=' ')
    print()
if __name__ == '__main__':
    
    tarr1 = array('i',[1,2,3,4,5])

    tarr1.append(15)
    print("After appending 15: ")
    show(tarr1)

    tarr1.insert(0,15)
    print(f"Inserting 15 before current tarr1[0] = {tarr1[0]}: ")
    show(tarr1)

    c=tarr1.count(15)
    print("Count of 15: ",c)

    i=tarr1.index(15)
    print("Index of 15: ",i)

    tarr1.extend([6,7,8,9,10,15])
    print("After extending the array with new values: ")
    show(tarr1)

    print("The popped value is: ",tarr1.pop())

    tarr1.remove(15)
    print("After removing the first occurence of 15: ")
    show(tarr1)

    tarr1.__delitem__(5)
    print("After deleting an item using index slicing: ")
    show(tarr1)

    L1 = tarr1.tolist()
    print("The new list is: ")
    show(L1)

    string = array.tobytes(tarr1).decode()
    print("The array in the form string is: ",string)

    tarr1.reverse()
    print("After reversing the array: ")
    show(tarr1)