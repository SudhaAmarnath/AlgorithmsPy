#{"denoms": [1, 5, 10, 25], "n": 10} #4 ways
#O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	nums = [0 for amount in range(n+1)] # number of coins
	nums[0] = 1 # total denom required to make 0 is 0
	for denom in denoms:
		for amount in range(1,len(nums)):
			if denom <= amount:
				nums[amount] += nums[amount - denom] #min of current amount and !+diff between n and denoms
	return nums[n]