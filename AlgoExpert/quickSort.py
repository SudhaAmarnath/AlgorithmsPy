# time O(n log n) | space O(log n)
def quickSort(s):
    # Write your code here.
    if len(s)<=1:
        return s
    else:
        pivot = s.pop()
    l1=[]
    l2=[]
    for i in s:
        if i > pivot:
            l1.append(i)
        else:
            l2.append(i)

    return quickSort(l2) +[pivot]+ quickSort(l1)