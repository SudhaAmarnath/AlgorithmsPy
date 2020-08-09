#https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)
        if x >= 0:
            reverse = int(s[::-1])
        else:
            reverse = -int(str(abs(x))[::-1])
        if reverse >= 2**31-1 or reverse <= -2**31:
            return 0
        else:
            return reverse