'''
https://leetcode.com/problems/coin-change-2/
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
'''
def count(coins, amount):

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    res = 0
    for i in range(len(coins)):
        res += count(coins, amount - coins[i])

    return res

if __name__ == '__main__':

    S = [1, 2, 3]
    N = 4

    print("Total number of ways to get desired change is", count(S, N))

#to reduce time complexity of the above code use hashmap
#memoization

def coincount(coins, amount, i ,d):
    def coincount(coins, amount, i, d):

        if amount == 0:
            return 1

        if amount < 0 or i < 0:
            return 0

        key = (i, amount)
        if key not in d:
            incl = coincount(coins, amount - coins[i], i, d)
            excl = coincount(coins, amount, i - 1, d)
            d[key] = incl + excl
        return d[key]

    if __name__ == '__main__':
        S = [1, 2, 3]
        N = 4
        d = {}
        print("Total number of ways to get desired change is", coincount(S, N, len(S) - 1, d))


#or using dynamic programming

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            j = coins[i]
            while j <= amount:
                dp[j] += dp[j - coins[i]]
                j += 1
        return dp[amount]
