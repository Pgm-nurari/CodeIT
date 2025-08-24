"""
To print the following pattern:
    *            1           1
   * *          2 2         1 2
  * * *        3 3 3       1 2 3
 * * * *      4 4 4 4     1 2 3 4
* * * * *    5 5 5 5 5   1 2 3 4 5
"""

n=int(input("Enter the number: "))
# Pattern 01
for i in range(1,n+1):
    space1 = n-i
    for j in range(1, space1+i+1):
        if j<=space1:
            print("",end = " ")
        else:
            print("*",end=" ")
    print()
    
# Pattern 02
for i in range(1, n+1):
    space1 = n-i
    for j in range(1,space1+i+1):
        if j>space1:
            print(i,end=" ")
        else:
            print("",end = " ")
    print()
# Pattern 03
for i in range(1, n+1):
    space1 = n-i
    c=1
    for j in range(1,space1+i+1):
        if j>space1:
            print(c,end=" ")
            c+=1
        else:
            print("",end = " ")
    print()