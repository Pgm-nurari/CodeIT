import os

def creating():
    os.system('clear')
    global list_01
    print("\n1.Using \'list()\' function.")
    list_01=list((1,2,3,4,5,6,7,8,9))
    print(f"list_01 is: {list_01}")
    list_01.clear()

    print("\n2.Using list comprehension")
    list_01=[i for i in range(0,100,2) if (i%4==0)]
    print(f"list_01 is: {list_01}")
    list_01.clear()

    print("\n3.Using for-loop.")
    print("Enter 5 values: ")
    for i in range(5):
        list_01.append(eval(input("Enter an element: ")))
    print(f"list_01 is: {list_01}")
    list_01.clear()    
    os.system("clear")

def functions():
    os.system("clear")
    print("\n::::____::::____Some List Functions_____::::_____::::\n")
    list_01=[i for i in range(1,11)]
    print(f"list_01 is: {list_01}")
    print("\n1.append()")
    list_01.append(11)
    print(f"list_01 is: {list_01}")
    print("\n2.extend()")
    list_01.extend([14,15])
    print(f"list_01 is: {list_01}")
    print("\n3.insert()")
    list_01.insert(13,[12,13])
    print(f"list_01 is: {list_01}")
    print("\n4.pop()")
    p=list_01.pop()
    print(f"list_01 is: {list_01}, and the popped element is {p}")
    print("\n5.pop(i)")
    p=list_01.pop(10)
    print(f"list_01 is: {list_01}, and the popped element is {p}")    
    print("\n6.remove(element)")
    list_01.remove(9)
    print(f"list_01 is: {list_01}")    
    print("\n7.reverse()")
    list_01.reverse()
    print(f"list_01 is: {list_01}")    
    print("\n8.count(element)")
    list_01.extend([1,3,4,1,1,3,4])
    c=list_01.count(1)
    print(f"list_01 is: {list_01}")
    print(f"count of 1 is: {c}")
    print("\n9.sort()")
    list_01.sort()
    print(f"list_01 is: {list_01}")    
    print("\n10.clear()")
    list_01.clear()
    print(f"list_01 is: {list_01}")
    print("\n11. del statement: ")
    del list_01
    try:
        print(f"list_01 is: {list_01}")        
    except:
        print("The list has been deleted permanently!!")

if __name__=='__main__':

    os.system("clear")