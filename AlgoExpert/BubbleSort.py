
#time O(n^2) space O(1)
def bubbleSort(s):
    # Write your code here.
    length = len(s)-1 #no comparision after last element
    sort = False
    while not sort:
        sort = True #iterate till sort = True
        for i in range(length):
            if s[i] > s[i+1]:
                sort = False #unsorted
                s[i],s[i+1]=s[i+1],s[i]
    return s

