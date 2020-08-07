#https://www.algoexpert.io/questions/Product%20Sum

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# time O(n) - number of elements counted as subarrays | space O(d) - max depth of subarray(recursive calls)
def productSum(array, multiplier=1):  # initial depth is one
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
