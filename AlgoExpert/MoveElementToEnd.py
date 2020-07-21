#solution1
#O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
	i = 0
    j = len(array)-1
    while i < j:
        while i < j and array[j] == toMove:
            j-=1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i+=1
    return array

#solution2
def moveElementToEnd(array, toMove):
    # Write your code here.

    arr1 = []
    arr2 = []
    for i in array:
        if i == toMove:
            arr1.append(i)
        else:
            arr2.append(i)

    return arr2 + arr1


'''

def movezero(s):

    arr = []

    for i in s:
        if i == 0:
            arr.append(i)
            s.remove(i)

    return s+arr
print(movezero([1,0,3,0,3,7,0]))

#or

def movezero(s):
    arr1 = []
    arr2 = []
    for i in s:
        if i > 0:
            arr1.append(i)
        else:
            arr2.append(i)

    return arr1 + arr2
print(movezero([1, 0, 3, 0, 3, 7, 0]))

#move nth element to last
def movetolast(s, n):
    last = s.index(n)
    s[-1], s[last] = s[last], s[-1]
    return s
print(movetolast([2,3,4,6,7],3)) #[2, 7, 4, 6, 3]
print(movetolast(['apple','cherry','kiwi','mango'],'apple')) #['mango', 'cherry', 'kiwi', 'apple']


'''

