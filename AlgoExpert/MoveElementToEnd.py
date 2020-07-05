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



