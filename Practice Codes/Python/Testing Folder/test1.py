import random

def checked():
    # Used to provide random values in the following range.
    for i in range(5):
        print(f"{i} {random.randrange(i,10)}") 

    # Used to generate random integer numbers in inclusive range.
    for j in range(5):
        print(j,end="\t")
        for i in range(1,random.randint(2,10)):
            print(random.randint(-10,10),end=' ')
        print()

    # Used to shuffle the list values
    test_list = [random.randint(-100,100) for i in range(10)]
    print(f"This is our original list: ",test_list)
    for i in range(5):
        random.shuffle(test_list) # Returns none, hence can't be used to print the shuffled list.
        print(test_list)

    # Used to select a few random elements from a sequence, with replacement of elemnts
    test_list = [random.randint(-100,100) for i in range(10)]
    print(f"The list is: {test_list}")
    print(f"5 selected elements from the above given list: {random.choices(test_list,k=5)}")

    # Used to select a few random elements from a sequence, without replacement of elemnts
    test_list = [random.randint(-100,100) for i in range(10)]
    print(f"The list is: {test_list}")
    print(f"5 selected elements from the above given list: {random.sample(test_list,k=5)}")

def main():
    print('testing the random module.')
    for i in range(5):
        for j in range(10):
            print("{:.2f}".format(random.uniform(-1.0,1.1)),end = " ")
        print()

if __name__=='__main__':
    main()