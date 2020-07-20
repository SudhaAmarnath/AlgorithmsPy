
#time O(n^2) | space O(1)

def selectionSort(s):
	length = len(s)-1
   # x = set() #to return non-duplicate elements

    for i in range(length):
        min = i #set default min value
        for j in range(i+1,len(s)):
            if s[j]<s[min]: #compare with the next element to the right
                min = j
        if min != i:
            s[min], s[i] = s[i], s[min] #swap if i is less than min value
        #for w in s:
            #if w not in x:
                #x.add(w)
    return s