'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8,4), (4,2),(8,2), (8,1), (4,1), (2,1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2)
'''

def countinversions(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] > s[j]:
                count += 1
    return count
print(countinversions([1, 20, 6, 4, 5]))

#or using mergesort
def merge(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        left, l = merge(left)
        right, r = merge(right)
        res = []
        i = 0
        j = 0
        inversions = 0 + l + r
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            inversions += (len(left)-i)
    res += left[i:]
    res += right[j:]
    return res, inversions
print(merge([ 1, 3, 5, 2, 4, 6 ]))


