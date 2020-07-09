'''
solution using hash map O(n) time.
determine if there is some subset of numbers in an array that can sum up to some number S.
arr = [1, 2, 3]
sum = 5
'''

def subsetProb(arr, s):
    d = {}
    for i in range(0,len(arr)):
        a = arr[i]
        b = s - a
        if b in d:
            return [a,b]
        else:
            d[a] = a