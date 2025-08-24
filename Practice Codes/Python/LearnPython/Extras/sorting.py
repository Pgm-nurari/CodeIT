import Modules.self_modules as sf
# Functions...

def bubble(L,l):
    print("\nThis is Bubble sorting\n")
    for i in range(0,l):
        for j in range(0,l-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    print("\nList after sorting is: ",L)            

def insertion(L,l):
    print("\nThis is Insertion sorting")
    for i in range(1,l):
        key=L[i]
        j=i-1
        while j>=0 and key<L[j]:
            L[j+1]=L[j]
            j=j-1
        else:
            L[j+1]=key
    print("\nlist after sorting is: ",L)

if __name__=='__main__':
    x=True
    while (x==True):
        print()
        ch=int(input("\nEnter your choice of sorting: \n1.Bubble\t\t2.Insertion\n"))
        match ch:
            case 1:
                L1=[]
                L1=sf.create_list();n1=len(L1);   bubble(L1,n1); x=True; break
            case 2:
                L2=[]
                L2=sf.create_list();n2=len(L2);   insertion(L2,n2); x=True; break
            case _:
                x=False
                break

