'''
Process and Sort Signal Strength Squares
You are working on a signal processing module for a weather satellite system. The system logs signal strengths as integers in a non-decreasing order. Due to certain transformations, you need to square each signal value and then reorganize the list to maintain non-decreasing order.

Write a program to take an array of sorted integers as input, square each number, and return the result as a sorted array.



Input Format

First line contains an integer n (1 ≤ n ≤ 10⁴) – number of signal values.
Second line contains n space-separated integers representing the array nums sorted in non-decreasing order (−10⁴ ≤ nums[i] ≤ 10⁴).


Output Format

Print the squared and sorted signal values as space-separated integers on a single line.


Example 1

Sample Input 1

5

-4 -1 0 3 10



Sample Output 1

0 1 9 16 100



Explanation

Squaring: [16, 1, 0, 9, 100]
Sorted output: [0, 1, 9, 16, 100]


Example 2

Sample Input 2

5

-7 -3 2 3 11



Sample Output 2

4 9 9 49 121



Explanation

Squaring: [49, 9, 4, 9, 121]
Sorted output: [4, 9, 9, 49, 121]
'''

def main():
    sentence = input()
    reversed = ""
    word=''
    for i in sentence:
        if not i.isalnum():
            reversed+=(word[::-1]+" ")
            word=''
        else:
            word+=i
        reversed+=(word[::-1])
    print(reversed)

if __name__ == "__main__":
    main() 