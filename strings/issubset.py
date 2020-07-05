for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))

#or

for _ in range(int(input())):
    a,A=int(input()),set(map(int,input().split()))
    b,B=int(input()),set(map(int,input().split()))
    if B==B.union(A):
        print(True)
    else:
        print(False)

'''
Strict superset
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Set  is the strict superset of the set but not of the set because  is not in set .
Hence, the output is False.
'''
A,l=set(map(int,input().split())),int(input())
for _ in range(1,l+1):
    a=set(map(int,input().split()))
    if A.issuperset(a):
        l-=1
if l==0:
    print('True')
else:
    print('False')