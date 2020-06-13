'''
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
------------------------------------------
BANANA FRIES: Quantity bought:1, Price: 12
Net Price: 12
POTATO CHIPS: Quantity bought:2 , Price: 30
Net Price: 60
APPLE JUICE: Quantity bought:2 , Price: 10
Net Price: 20
CANDY: Quantity bought:4 , Price: 5
Net Price: 20
'''

from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range(n):
    item = input().split(' ')
    price = int(item[-1])
    name = " ".join(item[:-1])
    if d.get(name):
        d[name] += price
    else:
        d[name] = price

for k,v in d.items():
    print(k,v)