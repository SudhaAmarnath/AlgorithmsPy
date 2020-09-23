#https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP/solutions
'''
For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

'''


def areSimilar(a, b):
    arr = [i for i in range(len(a)) if a[i] != b[i]]
    if len(arr) == 2:
        b[arr[0]], b[arr[1]] = b[arr[1]], b[arr[0]]
    return a == b