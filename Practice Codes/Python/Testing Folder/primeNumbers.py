
range_list = list(map(int,input().split()))
flag=0
if range_list[0]>=2:
    if range_list[0]%2==0:
        range_list[0] = range_list[0]+1
else:
    print(2,end=" ")
    range_list[0] = 3
for i in range(range_list[0],range_list[1]):
    flag=0
    for j in range(2,i):
        if i%j!=0:
            flag=0
        else:
            flag=1
            break
    if flag==0:
        print(i,end=" ")
    