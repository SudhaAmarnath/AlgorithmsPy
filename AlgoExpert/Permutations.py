#solution 1
def getPermutations(array):
    # Write your code here.
    from itertools import permutations
	if array == []:
		return []
    return [i for i in permutations(array)]


#solution 2
#time O(n*n!) | space O(n*n!)
def getPermutations(array):
    # Write your code here.
    permutations = []
	phelper(array, [], permutations)
	return permutations

def phelper(array, currentval, permutations):
	if not len(array) and len(currentval): # iterate till the list is empty, append final value
		permutations.append(currentval)
	else:
		for i in range(len(array)):
			newarray = array[:i] + array[i + 1 :]
			newpermutation = currentval + [array[i]]
			phelper(newarray, newpermutation, permutations)
