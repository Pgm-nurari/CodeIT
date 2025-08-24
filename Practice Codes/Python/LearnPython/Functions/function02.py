'''
[------------------------------]
 Function Overloading in Python
[------------------------------]

Python like C++/java does not support function overloading: instead we use *args and **kwargs

Wherein:
    *args => multiple arguments
    **kwargs => keyworded variable arguments

*args stores values as tuples inside a function.
**kwargs stores values as dictionaries inside a function.

When defining a function the order of args is:
    def function_name(arg1,def_arg,*args,**kwargs)

'''

def multiple_args(*b):
    """
    Use of multiple arguments!!!
    """
    print("Multiple Arguments Example")
    for item in b:
        print(item)

def kworded_args(**dict):
    """
    Use of kieyworded multiple arguments!!!
    """
    print("Keyworded variable Arguments Example")
    for i,j in dict.items():
        print(f"{i}\t{j}")

def functionName(number,*lst,**dict):
    """
    To show the order of args in the function.\n
    Enter the fieldnames as a list in place of *lst.\n
    Enter the first row details assigning them to their corresponding fieldnames.\n
    The row values can given in the last (**dict) in any order.
    Args:
        number (integer type): It should be the number of fields
    """
    print(f"number given is: {number}")
    print("\nThe Fields are: ")
    for item in lst:
        print(item)
    print("\nThe values are: ")
    for i,j in dict.items():
        print(f"{i}\t{j}")

if __name__ == '__main__':
    match(int(input("Enter the choice: "))):
        case 1:
            multiple_args(100,'percent was scored by','Neetu')
        case 2:
            kworded_args(one=1,two=2,three=3)
        case 3:
            functionName(3,['Employee_id','Employee Name','Salary'],Employee_id = 101,Employee_Name = 'Sabhyam' ,Salary = 90000)
        case _:
            print("Invalid Choice")