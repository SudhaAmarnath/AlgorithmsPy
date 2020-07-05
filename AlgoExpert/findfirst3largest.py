#to find the first 3 largest elements in a list
from heapq import nlargest

def largest(numbers):
    numbers = set(numbers)
    return nlargest(3,numbers)
print(largest([1,2,3,14,5,13,1]))