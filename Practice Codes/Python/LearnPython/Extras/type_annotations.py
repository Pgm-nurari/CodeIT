def variables() -> None:
    num : int = 10 
    word : str = 'testing'
    r_num: float = 16.5
    print(f"The value of num is {num}")
    print(f"Type of num is: {type(num)}")
    num:int = int(input("Enter a number: "))
    print(f"After giving a value of varying dataype in num, type of num is: {type(num)}: ")

def myfun(x: int, y: int) -> float:
    """
    This function takes two integers as input and returns their average
    """
    return  x/y

def sqrOfNumbers(*numbers: list[int]) -> list[int]:
    return [i**2 for i in numbers]

def main() -> None:
    variables()
    print(f"\nThe output of myfun(x,y) function is: {myfun(100,3)}")
    print(f"\nThe new list of squared numbers is: {sqrOfNumbers(1,2,3,4,5,6,7,8,9)}")

if __name__=='__main__':
    main()