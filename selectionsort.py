'''
Find the smallest element in the array. This smallest element is swapped with the first element. After this, search for the smallest element in the subarray formed by excluding the first element and compare it with the first element of the subarray. Repeat it till the array gets sorted.
'''
def selectionsort(s):
    length = len(s)-1
    x = set() #to return non-duplicate elements

    for i in range(length):
        min = i #set default min value
        for j in range(i+1,len(s)):
            if s[j]<s[min]: #compare with the next element to the right
                min = j
        if min != i:
            s[min], s[i] = s[i], s[min] #swap if i is less than min value
        for w in s:
            if w not in x:
                x.add(w)
    print(x)        #returns set {1, 2, 3, 5, 6, 8}
    print(list(x))  #returns list [1, 2, 3, 5, 6, 8]
    print(s)        #returns output of selection sort [1, 2, 3, 5, 6, 6, 8]
selectionsort([5,6,2,3,1,6,8])

