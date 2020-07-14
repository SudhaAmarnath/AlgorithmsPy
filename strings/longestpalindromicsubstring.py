'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        arr = ''
        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i, len(s)):

                str1 = s[i:j + 1]
                str2 = str1[::-1]
                #if len(str1) == 1:
                    #continue
                if str1 == str2 and len(str1) > count:
                    count = len(str1)
                    arr += str1
        return count #5

#to print all the palindromes
class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = []
        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i, len(s)):

                str1 = s[i:j + 1]
                str2 = str1[::-1]
                if str1 == str2:
                    arr.append(str1)
        print(arr)
Solution().longestPalindrome('acbcacb') #['a', 'acbca', 'c', 'cbc', 'b', 'bcacb', 'c', 'cac', 'a', 'c',

'''

#to get the len of LPS
#recursion
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n=len(s)
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            dp[i][i]=1
        for i in range(n-1,0,-1):
            for j in range(i+1,n+1):
                if s[i-1]==s[j-1]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[1][n]


#to get the LPS
#time O(n) space O(1)
#Manacher's Algorithm
#https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
#https://www.educative.io/edpresso/longest-palindromic-substring-in-on-with-manachers-algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=0
        L=0
        R=0
        for center in range(2*n-1):
            left=center//2
            right=left+center%2
            while left>=0 and right<n and s[left]==s[right]:
                if right-left>res:
                    res=right-left
                    R=right
                    L=left
                left-=1
                right+=1
        return s[L:R+1]

