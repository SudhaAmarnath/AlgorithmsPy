#time O(n) | space O(1)
#[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    # Write your code here.
    mainstr = 0
	substr = 0
	while mainstr < len(array) and substr < len(sequence):
		if array[mainstr] == sequence[substr]:
			substr += 1
		mainstr += 1
	return substr == len(sequence)

#or
#time O(n) | space O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
	l = 0
    for k,v in enumerate(array):
		if l == len(sequence):
			return True
		if sequence[l] == v:
			l+=1

	return l == len(sequence)

#or
##time O(n) | space O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
	seq = 0
    for v in array:
		if seq == len(sequence):
			return True
		if sequence[seq] == v:
			seq += 1

	return seq == len(sequence)
