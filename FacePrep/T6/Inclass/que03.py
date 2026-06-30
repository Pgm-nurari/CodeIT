"""
Smart Thief: Maximum Loot

A smart thief wants to rob houses along a street. Each house has some amount of money hidden inside, represented by an array. However, the thief cannot rob adjacent houses because the security system will alert the police.

Given an array representing the amount of money at each house, determine the maximum amount of money the thief can rob without alerting the police.



Input Format

The first line contains an integer n — the number of houses.
The second line contains n space-separated integers where each integer represents the amount of money in each house.


Constraints

1 <= n <= 100
0 <= money in each house <= 10^4


Output Format

Output a single integer — the maximum amount of money the thief can rob.


Example 1

Sample Input 1

6

6 7 1 3 8 2



Sample Output 1

15



Example 2

Sample Input 2

5

5 3 4 11 2



Sample Output 2

16



Explanation

Thief will steal from house 1 and 4, total money = 5 + 11 = 16.
"""

def max_sum_non_adjacent():
    n = int(input())
    arr = list(map(int,input().split()))

    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+arr[i])

    print(dp[n-1])
    
def optimized():
    n = int(input())
    arr = list(map(int,input().split()))

    f=0
    s=0
    for i in range(n):
        new=max(f,s+arr[i])
        s=f
        f=new
    print(f)