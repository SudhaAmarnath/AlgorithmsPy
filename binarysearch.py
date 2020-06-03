def binary_search(list, key):
    """
    Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
print(binary_search([7,11,13,15,23], 13))

#or

def binary_search(arr,val):
    n = len(arr)
    if n==0 or (n==1 and arr[0]!=val):
        return False
    mid = arr[n//2]
    if val == mid:
        return True
    elif val < mid:
        return binary_search(arr[:n],val)
    else:
        return binary_search(arr[n+1:],val)
print(binary_search([15,20,30,45,50],45))
