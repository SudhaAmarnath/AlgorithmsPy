'''
array1=[0, -6, 4, 6, 5, -2],
array2=[-4, 8, 2, 3, 10, 9]
the smallest difference between two elements of the two array is 1 with pairs (4, 3) from the arrays repectively.
'''

# O(nlgn)+O(n) = O(nlgn) time | O(1) space
def smallestDifference(array1, array2):
    # Write your code here.
    array1.sort()
    array2.sort()
    i = 0
    j = 0
    result = float("inf")
    mindiff = float("inf")
    # diff = 0
    while i < len(array1) and j < len(array2):
        diff = abs(array1[i] - array2[j])

        if (diff < mindiff):
            mindiff = diff
            min1 = array1[i]
            min2 = array2[j]

        if (array1[i] < array2[j]):
            i += 1
        else:
            j += 1

    return [min1, min2]