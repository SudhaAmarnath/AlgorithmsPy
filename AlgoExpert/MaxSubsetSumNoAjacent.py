#https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent
#O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	maxsum = array[:]
	maxsum[1] = max(array[0], array[1])
	for i in range(2, len(array)):
		maxsum[i] = max(maxsum[i - 1], maxsum[i - 2] + array[i])
	return maxsum[-1]