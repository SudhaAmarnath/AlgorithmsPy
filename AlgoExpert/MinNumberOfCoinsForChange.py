#time O(nd) - combinations, number of denominations | O(n) space complexity
def minNumberOfCoinsForChange(n, denoms): #total anount n and min number of coins required denom
		# Write your code here.
		nums = [float("inf") for amount in range(n+1)] # number of coins
		nums[0] = 0 # total denom required to make 0 is 0
		for denom in denoms:
			for amount in range(len(nums)):
				if denom <= amount:
					nums[amount] = min(nums[amount], 1 + nums[amount - denom]) #min of current amount and !+diff between n and denoms
		return nums[amount] if nums[amount] != float("inf") else -1 # if there is no possibility of denom the initial value = float("inf")