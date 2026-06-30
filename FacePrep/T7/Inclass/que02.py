"""
Plagiarism Detector: Finding the Longest Common Substring
You are part of a software development team building a plagiarism detection tool for universities. One critical feature of this tool is comparing two pieces of text (for example, student assignments) and identifying the longest continuous sequence of matching characters — i.e., the longest common substring — between them.

This feature helps quickly flag potentially copied sections where large identical blocks of text appear in both submissions.

Your task is to write a program that takes two input strings (representing two documents or code files) and returns the length of their longest common substring.



Remember

A substring is a continuous block of characters. For example, in "abcde", "bcd" is a substring, but "ace" is not (since it's non-contiguous).
Matching is case-sensitive (i.e., 'A' and 'a' are considered different).
If no common substring exists, the program should return 0.


Input Format

The first line contains the string s1 (document 1).
The second line contains the string s2 (document 2).


Constraints

0 ≤ s1.length, s2.length ≤ 1000
Both strings contain only uppercase and lowercase English letters.


Output Format

A single integer representing the length of the longest common substring between s1 and s2.


Example 1

Sample Input 1

abcdxyz

xyzabcd



Sample Output 1

4



Explanation

The longest common substring is "abcd", found at the end of s2 and the start of s1, with a length of 4.



Example 2

Sample Input 2

abc

(empty string)



Sample Output 2

0



Explanation

Since one string is empty, there are no common substrings, so the result is 0.
"""


def main():
    str1 = input()
    str2 = input()

    m=len(str1)
    n=len(str2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    ans = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                ans = max(dp[i][j], ans)

    print(ans)

def space_optimized():
    str1 = input()
    str2 = input()

    m=len(str1)
    n=len(str2)

    dp = [[0]*(n+1) for _ in range(2)]

    ans = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i%2][j] = 1+dp[(i-1)%2][j-1]
                ans = max(dp[i%2][j], ans)

    print(ans)
    
if __name__ == "__main__":
    main()    