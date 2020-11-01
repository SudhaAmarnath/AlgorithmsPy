
#https://www.algoexpert.io/questions/Min%20Number%20Of%20Jumps

# O(n^2) time | O(n) space
def minNumberOfJumps(array):
	arrlen = len(array)
	if arrlen == 1:
		return 0
    dp = [float("inf") for _ in range(arrlen)]
	dp[0] = 0
	for destIdx in range(1, arrlen):
		for sourceIdx in range(0, destIdx):
			if array[sourceIdx] >= destIdx - sourceIdx:
				dp[destIdx] = min(dp[destIdx], dp[sourceIdx] + 1)
	return dp[-1]
