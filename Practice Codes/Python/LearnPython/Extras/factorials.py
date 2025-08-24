def factorial(num):
    if num>1:
        return num*factorial(num-1)
    else:
        return 1
    

def main():
    print(factorial(5))
    pass


if __name__=='__main__':
    main()