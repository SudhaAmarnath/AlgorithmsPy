'''
>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}
'''
M,m=input(),set(list(map(int,input().split())))
N,n=input(),set(list(map(int,input().split())))
s = sorted(list(m.difference(n))+list(n.difference(m)))
for i in s:
    print (i)