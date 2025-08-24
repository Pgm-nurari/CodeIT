# User Definesd Functions and Doc_Strings..
import math

def functionOne(arg1,arg2): # non-return-type function
    """To print two values given as parameters
    Args:
        arg1 (_type_): Parameter 1
        arg2 (_type_): Parameter 2
    """
    print(f"This is a functon that prints the 2 given parameters: \nParameter01: {arg1}\nParameter02: {arg2}")

def functionTwo(a,b):
    addition = math.fsum([a,b])
    return addition

if __name__ == '__main__':

    functionOne('Hello','World')
    print("\nThe definition of functionOne() is:\n")
    print(functionOne.__doc__)
    print(f"The sum of 10 and 20 is: {functionTwo(10,20)}")
