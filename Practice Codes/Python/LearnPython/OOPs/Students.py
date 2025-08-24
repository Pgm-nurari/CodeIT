'''
A program to create an object of class Students and get values from the user:

1. Roll no.
2. Name
3. Batch
4. Stream
5. Mark1
6. Mark2
7. Mark3

Also create a method to print the values of the above.
'''

class Students:

    Inst_name = "Saraswathi Vidyanikethan School for Higher Studies" # Static variable.

    def __init__(self):
        '''
        Instance Variables Example.
        '''
        self.Roll_no = int(input("Enter the Roll no.: "))
        self.Name   = input("Enter the name: ")
        self.Batch  = int(input("Enter the Batch Year: "))
        self.Stream = input("Enter the stream: ")
        self.Mark1  = int(input("Enter mark1: "))
        self.Mark2  = int(input("Enter mark2: "))
        self.Mark3  = int(input("Enter mark3: "))

    def output(self):
        print("Batch year  ",self.Batch)
        print("Stream      ",self.Stream)
        print("Full name   ",self.Name)
        print("Roll_no     ",self.Roll_no)
        print("Mark 1      ",self.Mark1)
        print("Mark 2      ",self.Mark2)
        print("Mark 3      ",self.Mark3)
