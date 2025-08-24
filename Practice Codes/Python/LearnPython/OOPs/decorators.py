""" 
*Getters, Setters and Deleters
---------------------------
In Python, we can use the property() function to implement getters, setters and deleters for class variables.

*GETTER*
Allows the user to fetch values from the class.

*SETTER
Allows the users to enter data into the class variables without directly accessing them, as a property of the class. In setter the programmer can also include their own operations or functionalities. It is a good practice to use different names for properties, unlike the class variable names as it can help in establishing encapsulation in the code.

*DELETER
Allows the user to remove the value in the class variable

! We use them to encapsulate the essential data in the class by making it less accessible directly to the end-users or other external classes.

"""

class ContactInfo:

    def __init__(self):
        self.__objname: str = ''

    @property  # This is a property that can be used as a GETTER.
    def full_name(self):
        if self.__objname:
            return self.__objname
        else:
            return "Name is not set"

    @full_name.setter  #! This is a SETTER. Here we take value and perform a few operations on it.
    def full_name(self, value):
        try:
            if len(value) > 0 and isinstance(value, str) and value.isalpha():
                self.__objname = value
            else:
                raise ValueError("Invalid input. Please enter a valid name.")
        except ValueError as ve:
            print(ve)
        except TypeError:
            print("Invalid input. Please enter a string.")

    @full_name.deleter  #! This is a DELETER and can be used to apply deletion operations on the class variables.
    def full_name(self):
        if self.__objname == '':
            print("Name is already empty.")
        else:
            self.__objname = ''
            print("Name was removed!")

    def display(self):  #! Random method to display the class variable. Not related to Getters and Setters
        print(f"Accessing the '__objname' directly: {self.__objname}")

def main():
    obj = ContactInfo()
    obj.full_name = input("Enter a name: ")
    print(f"Getter has been called! {obj.full_name}")
    obj.display()
    if input("Do you want to delete the full_name? (yes/no): ") == "yes":
        del obj.full_name
        print(obj.full_name)
    else:
        print("Name was not deleted.")

if __name__ == "__main__":
    main()