'''
>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}
---------------------------------------------------------------------
>>> s = set("Hacker")
>>> print s.difference("Rank")
set(['c', 'r', 'e', 'H'])

>>> print s.difference(set(['R', 'a', 'n', 'k']))
set(['c', 'r', 'e', 'H'])

>>> print s.difference(['R', 'a', 'n', 'k'])
set(['c', 'r', 'e', 'H'])

>>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', 'H', 'k'])

>>> print s.difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'r'])

>>> s - set("Rank")
set(['H', 'c', 'r', 'e'])
--------------------------------------------------------
>>> H = set("Hacker")
>>> R = set("Rank")
H.update(R) = set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
H.intersection_update(R) = set(['a', 'k'])
H.difference_update(R) = set(['c', 'e', 'H', 'r'])
H.symmetric_difference_update(R) = set(['c', 'e', 'H', 'n', 'r', 'R'])
'''
M,m=input(),set(list(map(int,input().split())))
N,n=input(),set(list(map(int,input().split())))
s = sorted(list(m.difference(n))+list(n.difference(m)))
for i in s:
    print (i)

'''

M,m=input(),set(list(map(int,input().split())))
N,n=input(),set(list(map(int,input().split())))
print(len(m.intersection(n)))
print(len(m.union(n)))
print(len(m.difference(n)))

'''
