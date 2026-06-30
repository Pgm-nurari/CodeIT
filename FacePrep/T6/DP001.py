"""
Finding the nth Fibonacci number using Dynamic Programming (Memoization) and (Tabulation) approaches.
"""
n=int(input("Enter the position of the Fibonacci number: "))

def fib_recursive(n):
    dp = [-1]*(n+1)
    if n==0 or n==1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_recursive(n-1) + fib_recursive(n-2)
    return dp[n]

def fib_iterative(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fib_space_optimized(n):
    dp = [0]*(3)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
    return dp[n%3]

print(fib_recursive(n))
print(fib_iterative(n))
print(fib_space_optimized(n))
