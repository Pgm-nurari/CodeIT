"""
Maximum Profit from Non-Overlapping Jobs
You are working on a scheduling system for a freelance job platform. Each freelancer receives multiple job offers, where each job has a start time, an end time, and a profit if completed. Since a freelancer can only work on one job at a time, you need to help them maximize their profit by selecting a set of non-overlapping jobs.

Write a program that, given a list of jobs (with their start time, end time, and profit), finds the maximum total profit the freelancer can earn by selecting a set of non-overlapping jobs.



Note

If a job ends at time X, another job starting at time X is allowed.



Input Format

The first line contains an integer n, the number of jobs.
The next n lines each contain three integers: start, end, and profit, representing each job.


Constraints

1 ≤ n ≤ 1000
1 ≤ start < end ≤ 10^9
0 ≤ profit ≤ 10^4


Output Format

A single integer representing the maximum profit achievable without overlapping jobs.


Example 1

Sample Input 1

4

1 2 50

3 5 20

6 19 100

2 100 200



Sample Output 1

250



Explanation

The freelancer should pick jobs [1, 2] and [2, 100] for a total profit of 50 + 200 = 250.



Example 2

Sample Input 2

4

1 3 60

2 5 50

4 6 70

5 7 30



Sample Output 2

130



Explanation

The freelancer should pick jobs [1, 3] and [4, 6] for a total profit of 60 + 70 = 130.
"""

def greedy_job_scheduling(jobs):
    # Sort jobs based on their end time
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    dp = [0] * n  # dp[i] will store the maximum profit up to job i
    
    dp[0] = jobs[0][2]  # The profit of the first job
    
    for i in range(1, n):
        # Include the current job's profit
        include_profit = jobs[i][2]
        
        # Find the last non-overlapping job
        for j in range(i - 1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:  # If job j ends before job i starts
                include_profit += dp[j]
                break
        
        # Store the maximum of including or excluding the current job
        dp[i] = max(dp[i - 1], include_profit)
    
    return dp[-1]  # The maximum profit is stored in the last element

def dynamic_programming_job_scheduling(jobs):
    # Sort jobs based on their end time
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    dp = [0] * n  # dp[i] will store the maximum profit up to job i
    
    dp[0] = jobs[0][2]  # The profit of the first job
    
    for i in range(1, n):
        # Include the current job's profit
        include_profit = jobs[i][2]
        
        # Find the last non-overlapping job using binary search
        low, high = 0, i - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[i][0]:  # If job mid ends before job i starts
                include_profit += dp[mid]
                low = mid + 1
            else:
                high = mid - 1
        
        # Store the maximum of including or excluding the current job
        dp[i] = max(dp[i - 1], include_profit)
    
    return dp[-1]  # The maximum profit is stored in the last element

def main():
    pass
if __name__ == "__main__":
    main()
