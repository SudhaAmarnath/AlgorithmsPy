'''
https://leetcode.com/problems/validate-ip-address/
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


#or

class Solution:
    def validIPAddress(self, IP: str) -> str:
        res = 0
        ipv4 = IP.split('.')
        if len(ipv4) == 4:
            for x in ipv4:
                if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                    res = 1
                    break
            if not res:
                return 'IPv4'

        ipv6 = IP.split(':')
        if len(ipv6) == 8:
            for x in ipv6:
                if x == '' or len(x) > 4 or not all(c in hexdigits for c in x):
                    res = 1
                    break
            if not res:
                return 'IPv6'

        return 'Neither'

#or regex : O(1) O(1)
class Solution:
    def validIPAddress(self, IP: str) -> str:
        import re

        ipv4_pattern = r"^\b([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b$"

        ipv6_pattern = r"^([a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$"

        ipv4_obj = re.search(ipv4_pattern, IP)
        ipv6_obj = re.search(ipv6_pattern, IP)

        if ipv4_obj:
            return "IPv4"
        if ipv6_obj:
            return "IPv6"

        return "Neither"