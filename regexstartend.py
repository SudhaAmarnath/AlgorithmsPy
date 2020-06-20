'''
Sample Input

aaadaa
aa
Sample Output

(0, 1)
(1, 2)
(4, 5)


>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
'''


import re
s = input()
v = input()
for i,x in enumerate(s):
    if re.match(v,s[i:]):
        print((i,i+len(v)-1))
if re.search(v, s)==None:
    print((-1,-1))