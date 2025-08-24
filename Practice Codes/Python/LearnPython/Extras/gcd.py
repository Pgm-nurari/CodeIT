def gcd(a,b):
    if a<b:
        low=a
    else:
        low=b
        
    hcf=1
    for i in range(1,low+1):
        if a%i==0 and  b%i==0:
            hcf=i
    return hcf

def main():
    x,y=int(input("Enter number 1: ")),int(input("Enter number 2: "))
    if x>0 and y>0 :
        c=gcd(x,y)
    print(f"The gcd of {x}, {y} is {c}")
    
    
if __name__=='__main__':
    main()