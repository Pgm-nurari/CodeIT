'''
Different types of variables in a class:

1. Instance Variables ( Refer to the variables in init() in the module Students.py file.)
2. Class or Static Variables

'''

class second_class:
    st_var1 = 0
    st_var2 = 0

    def __init__(self):
        self.ins_var1= input("Instance Entry no. 1: ")
        self.ins_var2= input("Instance Entry no. 2: ")

    def static_variables01(self):
        second_class.st_var1 = input("Static Entry no. 1: "); 
        ''' 
        Giving the <class_name> itself instead of
        passing "cls" as an argument is a good practice
        '''
        second_class.st_var2 = input("Static Entry no. 2: ")
        print("Instance variables are:\nvar1 = {}\nvar2 = {}".format(self.ins_var1,self.ins_var2))
        print("Static variables are:\nst_var1 = {}\nst_var2 = {}".format(second_class.st_var1,second_class.st_var2))
        

def main():
    obj1 = second_class()
    obj1.static_variables01()

if __name__ == '__main__':
    main()