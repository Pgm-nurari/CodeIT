'''
Constructor in Inheritance 1

by default the computer fetches the constructor of only child class,
if it does not exist it goes for the parent class's constructor.

but, what if child class has its own constructor and still wants to access the
constructor of the parent class? Look below at the code...

'''
class parent:

    def __init__(self) -> None:
        print("Inside parent class")

    def feature1(self):
        print("Feature one working")
    def feature2(self):
        print("Feature two working")

class child1 (parent):

    def __init__(self) -> None:
        super().__init__()              # To call the constructor of parent class
        print("Inside child1 class")

    def feature3(self):
        print("Feature three working")
    def feature4(self):
        print("Feature four working")
