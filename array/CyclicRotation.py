#shifting last K elements of the array and moving them to the front

#Solution 1
def CyclicRotation(arr, k):
    n = len(arr)
    b = [0] * n
    for i in range(n):
        b[i] = arr[(i-k) % n]
    return b
print(CyclicRotation([2,3,4,0,1],3))#[9,7,6,3,8]

#solution 2
def CyclicRotation(arr, k):
    if len(arr) == 0:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

