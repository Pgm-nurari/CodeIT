def hourGlassSum():
    matrix = [
        [1,0,0,1,0,0],
        [2,0,0,1,0,0],
        [1,1,1,1,1,1],
        [2,1,1,1,1,0],
        [1,0,0,1,1,1],
        [2,1,0,1,1,1]
    ]
    count = 0
    max = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                new_list = [matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j+1], matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
                if (sum(new_list)>=max):
                    max = sum(new_list)
                    print(f"{matrix[i][j]} {matrix[i][j+1]} {matrix[i][j+2]}\n  {matrix[i+1][j+1]}\n{matrix[i+2][j]} {matrix[i+2][j+1]} {matrix[i+2][j+2]}")
                    count+=1
                    print("Hour glass number:", count)
                
                
            except:
                continue
    print(f"Maximum value in any hour glass: {max}")

def diagnolSum():
    n = int(input())
    matrix=[]
    for _ in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    sum = 0
    for i in range(n):
        sum+=matrix[i][i]

    print(sum)

def arrayUnionIntersection():
    pass

def main():
    hourGlassSum()

if __name__=='__main__':
    main()