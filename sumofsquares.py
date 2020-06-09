
def sumofsquares(alist):
    return (sum([i**2 for i in alist]))

print(sumofsquares([1,2,3,4,5]))

'''
l=[1,2,3,4,5]
sum=0

for i in l:
    sum+=i*i
print(sum)
'''
'''
Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
output 
206
'''
from itertools import product

n,p = map(int,input().split())
m = (list(map(int, input().split()))[1:] for _ in range(n))
results = map(lambda x: sum(i**2 for i in x)%p, product(*m))
print(max(results))
