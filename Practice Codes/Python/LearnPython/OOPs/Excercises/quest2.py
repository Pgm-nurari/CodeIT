class Animal:
    animal_type = "Plingers"
    def __init__(self):
        self.animal_type = ""
def main():
    obj1 = Animal()
    obj1.animal_type = "Elephant"
    print(f"Class variable has value: {Animal.animal_type}")
    print(f"Object variable has value {obj1.animal_type}")

if __name__=='__main__':
    main()