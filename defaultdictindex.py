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
'''
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n + 1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)