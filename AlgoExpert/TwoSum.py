#using 2 for loops
#time O(n^2) space O(n)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == targetSum:
                return [array[i],array[j]]
    return []


#using map
#time O(n) space O(n)
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
	for num in array:
		if targetSum - num in nums:
			return [targetSum - num, num]
		else:
			nums[num] = True
            #nums[num] = num
	return []

#or using itertools
def twoNumberSum(array, targetSum):
	import itertools
	for i in itertools.combinations(array,2):
		if i[0] + i[1] == targetSum:
			return i
	return []
