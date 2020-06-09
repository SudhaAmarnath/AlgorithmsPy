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