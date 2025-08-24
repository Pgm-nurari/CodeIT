'''
Class inside a Class...
'''

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop :
        def __init__(self) -> None:
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '16gb'
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('sabhyam',19)
s2 = Student('suraj',20)

s1.show()
'''
lap1 = s1.Laptop()
# or
lap2 = Student.Laptop()
'''
