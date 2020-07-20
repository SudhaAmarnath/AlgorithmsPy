
#time O(n^2) | space O(1)

def insertionSort(s):
    # Write your code here.
    length = range(1,len(s))
    for i in length:
        val1 = s[i]
        while s[i-1] > val1 and i>0:
            s[i],s[i-1] = s[i-1],s[i]
            i-=1
    return s