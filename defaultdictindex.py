'''
Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print .
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)

result

'''
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n + 1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)

'''
('a', [0, 1, 6])
('b', [2, 3])
('c', [10, 11, 12])
('d', [9, 13])
('e', [4, 7, 14])
('f', [5, 8, 15])

from collections import defaultdict

def duplicatepos(s):
    d = defaultdict(list)
    for i,item in enumerate(s):
        d[item].append(i)
    return ((k,v) for k,v in d.items()
                            if len(v)>1)

for j in sorted(duplicatepos('aabbefaefdcccdefs')):
    print(j)

#or


'''