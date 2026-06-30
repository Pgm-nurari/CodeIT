"""
Robot’s Grid Navigation Challenge

A robot is placed in the top-left corner of an m x n grid.
It can move only right or down from its current cell.
Your task is to compute the total number of unique paths the robot can take to reach the bottom-right corner of the grid.

Input Format
The first line contains two integers m and n — the number of rows and columns of the grid.
Constraints
1 <= m, n <= 100
Output Format
Output a single integer — the total number of unique paths from the top-left to the bottom-right.

Example 1
Sample Input 1
2 2

Sample Output 1
2

Explanation
The robot can take the following paths:
(0, 0) → (0, 1) → (1, 1)
(0, 0) → (1, 0) → (1, 1)



Example 2
Sample Input 2
2 3

Sample Output 2
3

Explanation
The robot can take the following paths:
(0, 0) → (0, 1) → (0, 2) → (1, 2)
(0, 0) → (0, 1) → (1, 1) → (1, 2)
(0, 0) → (1, 0) → (1, 1) → (1, 2)
"""

def space_optimized_unique_paths(m, n):
    m,n = map(int,input().split())
    dp = [1]*n

    for i in range(1,m):
        for j in range(1,n):
            dp[j] = dp[j] + dp[j-1]

    print(dp[n-1])

def main():
    m,n = map(int,input().split())
    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        dp[i][0] = 1
    for j in range (n):
        dp[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[m-1][n-1])

if __name__ == "__main__":
    main()