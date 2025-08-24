'''
This is a test_class...
'''

class first_class:
    def __init__(self):
        print(f"Package name is {__package__}")
        print(f"Module name is {(__name__.split('.'))[0]}")
        print(f"Class name is {__class__.__name__}") # type(<object_name>.__name__)

    def output1(self):
        print("This is a function output1")
    def output2(self):
        print("This is a function output2")
def main():

    tc1 = first_class()
    first_class.output1(tc1)
    tc1.output2()

if __name__ == '__main__':
    main()