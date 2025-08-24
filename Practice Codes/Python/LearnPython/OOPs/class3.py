'''
[----------------]
 Types of Methods
[----------------]
There are 3 types of methods in a class, they are:
1.  Instance methods: methods that take "self" as the first argument. Appplied on instance variables.
2.  Class methods: methods that can only be used in the class and do not vary based on the instances of the classes.
They use the class/static variables.
3.  Static methods: methods that may be declared inside a class but they operate like a normal function.
4.  Giving the <class_name> itself instead of
        passing "cls" as an argument is a good practice

'''
class function_class:
    count = 0
    def __init__(self,var1,var2):
        function_class.count += 1
        self.var1 = var1
        self.var2 = var2
    def sum(self):
        self.res1 = self.var1 + self.var2
        return self.res1

    @classmethod
    def concat(cls):
        cls.integer1 = input("Entre a number: ")
        cls.integer2 = input("Entre a number: ")
        return cls.integer1 + cls.integer2

    @staticmethod
    def object_count():
        return function_class.count