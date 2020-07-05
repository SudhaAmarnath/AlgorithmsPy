'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of c
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount                                # fill invalid amount i.e amount + 1 for all amounts ranging from 0 to amount.
        dp[0] = 0
        for value in range(amount+1):                                   # for each value till amount
            for coin in (coins):                                        # for each coin
                if(coin <= value):                                      # check if this coin can be used make value i.
                    dp[value] = min(dp[value], 1 + dp[value - coin])    # 1 => current coin included, check the min coins required to make remaining value i.e  value - coin
        return -1 if(dp[amount] > amount) else dp[amount]