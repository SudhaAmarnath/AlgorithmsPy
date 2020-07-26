def getPermutations(array):
    # Write your code here.
    from itertools import permutations
	if array == []:
		return []
    return [i for i in permutations(array)]