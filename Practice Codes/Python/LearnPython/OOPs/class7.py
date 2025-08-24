'''
Constructor in Inheritance 2

Method Resolution Order (MRO) :

When we perform multi-level inheritance and need a prent class's constructor,
using super() method, will only fetch the left_most parent class's contructor (that is deifned while inheriting in the paranthesis)
and then it moves towards other classes.

This order of fetching constructors or methods (with same name) from parent classes is from left to right,
also known as MRO

'''
class A:

    def __init__(self) -> None:
        print("Inside A class")

    def feature1(self):
        print("Feature 1-A working")
    def feature2(self):
        print("Feature two working")

class B ():

    def __init__(self) -> None:
        print("Inside B class")

    def feature1(self):
        print("Feature 1-B working")
    def feature4(self):
        print("Feature four working")

class C(A,B):

    def __init__(self) -> None:
        super().__init__()
        print("Inside C class")

    def feature5(self):
        print("Feature one working")
    def feature6(self):
        print("Feature two working")

    def fetch(self):
        super().feature2() # fetching a parent method

def main():
    c1 = C()
    c1.feature1()
    c1.fetch()

if __name__ == '__main__':
    main()