#longest substring without repeating chracters
'''
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class substirngcount:
    def subs(self,s: str)->int:
        start = 0
        maxlen = 0
        d = {}
        for end in range(len(s)):
            if s[end] in d and start <= d[s[end]]:
                start = d[s[end]]+1
            else:
                maxlen = max(maxlen, end-start+1)
            d[s[end]] = end
        return maxlen
print(substirngcount().subs('abcabcbb'))