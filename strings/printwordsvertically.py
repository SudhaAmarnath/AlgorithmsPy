#https://leetcode.com/problems/print-words-vertically/submissions/
'''
Input
"HOW ARE YOU"

Output
["HAY","ORO","WEU"]
'''

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxl = max([len(x) for x in s])
        res = maxl * [""]
        for j in range(maxl):
            for i in range(len(s)):
                if len(s[i]) <= j:
                    res[j] += ' '
                else:
                    res[j] += s[i][j]
            if res[j][-1] == ' ':
                res[j] = res[j].rstrip()
        return res