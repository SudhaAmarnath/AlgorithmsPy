'''
Sample Input

3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329
Sample Output

Neither
IPv4
IPv6  
'''

import re

n = int(input())

for n in range(n):
    string = input()
    if re.search(r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$', string):
        print('IPv6')
    elif re.search(r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', string):
        print('IPv4')
    else:
        print('Neither')