"""
Mission Backpack: Find the Secret Subset

You are given a list of artifacts, each with a weight value.

Your goal is to determine if there is a subset of artifacts such that the total weight equals a given target weight.

You can either include or exclude each artifact individually.

Return True if such a subset exists, otherwise return False.



Input Format

The first line contains two integers n and sum — the number of artifacts and the target weight sum.
The second line contains n space-separated integers representing the weight values of the artifacts.


Constraints

1 <= n <= 100
0 <= weight value <= 10^4
0 <= sum <= 10^4


Output Format

Output True if a subset with the given sum exists, otherwise output False.


Example 1

Sample Input 1

6 9

3 34 4 12 5 2



Sample Output 1

true



Explanation

The subset {4, 5} adds up to 9.



Example 2

Sample Input 2

6 30

3 34 4 12 5 2



Sample Output 2

false



Explanation

There is no subset that adds up to 30.
"""

def baktrack(n, k, arr):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))

    dp=[False]*(k+1)
    dp[0]=True

    for i in range(n):
        for j in range(k,arr[i]-1,-1):
            dp[j]=dp[j] or dp[j-arr[i]]

    if dp[k] == True:
        print('true')
    else:
        print('false')