"""
Identify Zero-Sum Triplets in an Array

You are working as a developer for a financial analytics firm that processes large datasets of integer values representing daily profit and loss figures. Your task is to identify any three distinct entries in the dataset that together result in a net gain/loss of zero.

Write a program to return all unique triplets from the array such that the sum of the triplet is zero. Each triplet should be in non-descending order, and the list should not contain duplicate triplets.



Input Format

First line contains an integer n (3 ≤ n ≤ 10⁴) – number of elements in the array.
Second line contains n space-separated integers representing the array nums (−10⁵ ≤ nums[i] ≤ 10⁵).


Output Format

Print all unique triplets that sum to zero. Each triplet should be printed on a separate line in increasing order.


Example 1

Sample Input 1

6

-1 0 1 2 -1 -4



Sample Output 1

-1 -1 2

-1 0 1



Explanation

Valid triplets:
(-1) + (-1) + 2 = 0
(-1) + 0 + 1 = 0
Duplicates like [-1, 2, -1] are avoided due to sorting and set usage.
"""

def non_optimized_solution():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    # print(*arr)
    res=[]
    for i in range(n-2):
        if arr[i]>0:
            break
        p1=i+1
        p2=n-1
        while p1<p2:
            total=arr[i]+arr[p1]+arr[p2]
            if total==0:
                res.append((arr[i], arr[p1], arr[p2]))
                p1+=1
                p2-=1
            elif total<0:
                p1+=1
            else:
                p2-=1
    res=list(set(res))
    res.sort()
    for i in res:
        print(*i)

def optimized_solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    for i in range(n - 2):
        # Skip duplicate values for the first element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
            
        # Optimization: If the smallest number is greater than 0, 
        # no three numbers can ever sum to 0.
        if arr[i] > 0:
            break

        # Initialize two pointers
        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                print(arr[i], arr[left], arr[right])
                left += 1
                right -= 1
                
                # Skip duplicate values for the left pointer
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                # Skip duplicate values for the right pointer
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
                    
            elif total < 0:
                # The sum is too small; move the left pointer forward to get a larger value
                left += 1
            else:
                # The sum is too large; move the right pointer backward to get a smaller value
                right -= 1

def main():
    # optimized_solution()
    # non_optimized_solution()
    pass

if __name__ == "__main__":
    main()
