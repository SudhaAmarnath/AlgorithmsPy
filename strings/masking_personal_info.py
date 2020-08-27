#https://leetcode.com/problems/masking-personal-information/submissions/
class Solution:
    def maskPII(self, S: str) -> str:

        if "@" in S:
            arr = S.split("@")
            arr[0] = (arr[0][0] + "*****" + arr[0][-1]).lower()
            arr[1] = arr[1].lower()
            return "@".join(arr)
        else:
            temp = ""

            for i in range(len(S)):
                if S[i].isnumeric():
                    temp += S[i]

            if len(temp) == 10:
                temp = "***-***-" + temp[6:]
            else:
                cc = len(temp) - 10
                temp = "+" + "*" * cc + "-***-***-" + temp[6 + cc:]

            return temp