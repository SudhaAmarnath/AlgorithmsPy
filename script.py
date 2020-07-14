# Utility function to swap two elements A[i] and A[j] in the list
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Linear-time partition routine to sort a list containing 0, 1 and 2
# It similar to three-way Partitioning for Dutch national flag problem
def threeWayPartition(A, end):

    start = mid = 0
    pivot = 1

    while mid <= end:
        if A[mid] < pivot:    # current element is 0
            swap(A, start, mid)
            start = start + 1
            mid = mid + 1
        elif A[mid] > pivot:  # current element is 2
            swap(A, mid, end)
            end = end - 1
        else:                 # current element is 1
            mid = mid + 1


# Sort a list containing 0’s, 1’s and 2’s
if __name__ == '__main__':

    A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    threeWayPartition(A, len(A) - 1)
    print(A)
