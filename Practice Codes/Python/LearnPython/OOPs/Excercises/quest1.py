"""
Question 1 from Excercises
"""

class Question1:
    """
    A class to get user input...!
    """
    def __init__(self) -> None:
        self.var1=''
    def get_input(self):
        self.var1 = input("Enter something here: ")
    def print_input(self):
        print(f"The text you entered is: {self.var1}")

def main():
    obj1 = Question1()
    obj1.get_input()
    obj1.print_input()

if __name__=='__main__':
    main()