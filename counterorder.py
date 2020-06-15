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