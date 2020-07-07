'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def myadd(c, d):
            while d != 0:
                c, d = c^d, (c&d)<<1
            return c
        if a < 0 and myadd(~a, 1) <= b or b < 0 and myadd(~b, 1) <= a:
            return ~myadd(myadd(~a, ~b), 1)
        return myadd(a, b)