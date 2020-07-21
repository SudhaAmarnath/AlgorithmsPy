#to find the first 3 largest elements in a list

from heapq import nlargest
def findThreeLargestNumbers(array):
    # Write your code here.
	return sorted(nlargest(3,array))


#or
from heapq import nlargest
def largest(numbers):
    numbers = set(numbers)
    return nlargest(3,numbers)
print(largest([1,2,3,14,5,13,1]))

#or
def findThreeLargestNumbers(array):
    # Write your code here.
	# return sorted( [x for i,x in enumerate(array)], reverse=True )[:3]
    lst = sorted( [x for i,x in enumerate(array)], reverse=True )[:3]
	return sorted(lst)

#or to remove duplicate
def findThreeLargestNumbers(array):
	n = list()
    lst = sorted( [x for i,x in enumerate(array)], reverse=True )[:3]
	for x in lst:
		if x not in n:
			n.append(x)
	return sorted(n)

#or using set
def findThreeLargestNumbers(array):
    n = set(array)
    lst = sorted( [x for i,x in enumerate(array)], reverse=True )[:3]
    for x in lst:
        n.add(x)
        return sorted(n)
print(findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 9])) #[7,8,9]