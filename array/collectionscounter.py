'''
Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  200
Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
from collections import Counter
_ = int(input())
itemlist = list(map(int,input().split()))
sizecount = Counter(itemlist)
sales = 0
for _ in range(int(input())):
    size, price = map(int,input().split())
    if(size in sizecount.elements()):
        sales+=price
        sizecount[size]-=1
print(sales)