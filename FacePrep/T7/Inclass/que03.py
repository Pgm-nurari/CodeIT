"""
Unique Paths in a Grid with Obstacles
You are developing a navigation system for delivery robots inside a warehouse. The warehouse is represented as a 2D grid of size m x n, where each cell can either be empty (0) or contain an obstacle (1).

The robot starts at the top-left corner (1, 1) and must reach the bottom-right corner (m, n). It can only move right or down at any point.

Your task is to write a program that calculates the number of unique paths the robot can take to reach the destination without passing through obstacles.



Input Format

The first line contains two integers m and n (number of rows and columns).
The next m lines each contain n integers (0 or 1), representing the grid.


Constraints

1 ≤ m, n ≤ 100
grid[i][j] ∈ {0, 1}


Output Format

A single integer representing the number of unique paths from the top-left corner to the bottom-right corner, avoiding obstacles.


Example 1

Sample Input 1

3 3

0 0 0

0 1 0

0 0 0



Sample Output 1

2



Explanation

There are two valid paths:

Right → Right → Down → Down
Down → Down → Right → Right


Example 2

Sample Input 2

2 2

0 1

0 0



Sample Output 2

1



Explanation

There is only one valid path:

Down → Right
"""

def main():
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]

    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        print(0)
        return

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    print(dp[m-1][n-1])
    
if __name__ == "__main__":
    main()