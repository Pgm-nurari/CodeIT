"""
Freelancer Task Scheduler: Maximizing Profit with Deadlines

You are building a task scheduler for a freelance job portal. Each job on the platform has:

A unique job ID.
A deadline (the last day it can be completed).
A profit (how much money it pays if completed).
A freelancer can only work on one job per day, and each job takes exactly one day to complete. The goal is to schedule jobs such that the total profit is maximized, and no job is scheduled after its deadline.

You are given a list of jobs with their deadlines and profits. Your task is to return the maximum number of jobs that can be completed and the total profit earned.



Input Format

The first line contains an integer n, the number of jobs.
The next n lines contain three space-separated values for each job:
A string jobId, an integer deadline, and an integer profit.


Output Format

Two space-separated integers:
The maximum number of jobs that can be done.
The maximum profit earned.


Example 1

Sample Input 1

4

a 4 20

b 1 10

c 1 40

d 1 30



Sample Output 1

2 60



Explanation

We can do at most 2 jobs.
Choose jobs c (profit 40, deadline 1) and a (profit 20, deadline 4).
Total profit = 40 + 20 = 60.


Example 2

Sample Input 2

5

j1 2 100

j2 1 19

j3 2 27

j4 1 25

j5 3 15



Sample Output 2

3 142



Explanation

Selected jobs: j1 (100), j3 (27), j5 (15)
Maximum profit = 142
Maximum jobs = 3
"""

def main():
    n = int(input())
    jobs = []
    
    for _ in range(n):
        jobId, deadline, profit = input().split()
        jobs.append((jobId, int(deadline), int(profit)))
    
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * (max_deadline + 1)  # Track occupied slots
    total_profit = 0
    job_count = 0
    
    for jobId, deadline, profit in jobs:
        # Find a free slot for this job (starting from its deadline)
        for d in range(min(max_deadline, deadline), 0, -1):
            if not slots[d]:  # If the slot is free
                slots[d] = True  # Mark this slot as occupied
                total_profit += profit
                job_count += 1
                break
    
    print(job_count, total_profit)
    
if __name__ == "__main__":
    main()