'''
HACK 3
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

s,n=input().split()
from itertools import permutations
l=list(permutations(sorted(s),int(n)))
for i in l:
    print("".join(i))

#itertools cartesian product

'''
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]


A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
'''
from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))