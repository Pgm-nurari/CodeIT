'''
Inheritance
'''

class parent:
    def feature1(self):
        print("Feature one working")
    def feature2(self):
        print("Feature two working")

class child1 (parent):
    '''
    Single Level Inheritance
    '''
    def feature3(self):
        print("Feature three working")
    def feature4(self):
        print("Feature four working")

class child2 (child1):
    '''
    multi Level Inheritance
    '''
    def ability1(self):
        print("ability one working")

    def ability2(self):
        print("ability two working")

class other_child:
    def feature(self):
        print("This is feature from other_child class")

class grand_child (child1,other_child):
    '''
    Multiple Inheritance
    '''
    def feature5(self):
        print("Feature five working")

p1 = parent()

c1 = child1()
c2 = child2()

gc1 = grand_child()
