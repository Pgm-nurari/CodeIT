from Modules.self_modules import single_list as sl
from collections import defaultdict

#program to remove duplicate elements from list

def default_value():
    return 0 

def method_01(L2):
    L3=[]
    for i in range(0,len(L2)):
        if L2[i] in L3:
            continue
        else:
            L3.append(L2[i])
    print(L3)

def method_02(L2):
    print(list(set(L2)))

def method_03():
    l=sl()
    mydict=defaultdict(default_value)
    for i in l:
        if mydict[i]==1:
            l.remove(i)
        else:
            mydict[i]=1
    print(l)

def method_04():
    l=sl()
    nl=list(dict.fromkeys(l))
    print(l)
    print(nl)
    
if __name__=='__main__':
    x=0
    while(x==0):
        print("This is method_03: \n")
        method_03()
        x=int(input("Enter [0] to continue: "))