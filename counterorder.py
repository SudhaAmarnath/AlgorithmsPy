def counterorder(s):

    from collections import Counter
    c=Counter(sorted(s)).most_common(3)
    for i in c:
        print(*i)
counterorder('aabbcccccdddd')
counterorder('123231112334')

'''
c 5
d 4
a 2
1 4
3 4
2 3
'''

#to print only the duplicates in the elements

s = '12343545456'
#s = [1,2,3,4,4,5,5,5,5,6,1,3]
print([i for i in set(s) if s.count(i)>1]) #['4', '3', '5']
