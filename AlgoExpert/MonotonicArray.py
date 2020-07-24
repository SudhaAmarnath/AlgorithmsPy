#Solution1
# time O(n) | space O(1)
def isMonotonic(A):
    # Write your code here.

    increasing = decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            increasing = False
        if A[i] < A[i + 1]:
            decreasing = False

    return increasing or decreasing

#solution2
#time O(n) | space O(1)
def isMonotonic(A):
    # Write your code here.
	return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or all(A[i] >= A[i+1] for i in range(len(A) - 1)))
