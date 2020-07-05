#select a pivot element in the list and create 2 lists for lower and greater values comparing to pivot
def quicksort(s):
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

    return quicksort(l2) +[pivot]+ quicksort(l1)

print(quicksort([2,25,6,15,8]))


