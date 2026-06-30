"""
Robot Staircase Climb

A robot is programmed to climb a staircase. The robot can move either 1 step or 2 steps at a time.

Given n steps in the staircase, determine how many distinct ways the robot can reach the top.

The robot can take the steps in any combination — for example, it can take two 1-steps or one 2-step to cover 2 stairs.



Input Format

The first line contains an integer n — the total number of steps.



Constraints

1 <= n <= 45


Output Format

Output a single integer — the number of distinct ways the robot can climb to the top.


Example 1

Sample Input 1

2



Sample Output 1

2



Explanation

There are two ways to climb 2 steps:

1 step + 1 step
2 steps


Example 2

Sample Input 2

3



Sample Output 2

3



Explanation

There are three ways to climb 3 steps:

1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
"""


def main():
    n=int(input())
    
    dp = [-1]*(3)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
      dp[i%3]=dp[(i-1)%3] + dp[(i-2)%3]
    
    print(dp[n%3])

if __name__ == "__main__":
    main()