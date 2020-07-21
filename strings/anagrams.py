#set of strings containg same characters but different order
#example "tide" and "diet"are anagrams of each other
def is_anagram1(s1,s2):
    h = {}
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    for ch in s1:
        if ch not in h:
            h[ch]=0
        h[ch]+=1
    for ch in s2:
        if ch not in h:
            h[ch]=0
        h[ch]-=1
    for key in h.keys():
        if h[key]!=0 or len(s1)!= len(s2):
            return False
        return True
print(is_anagram1("tictac","tactic"))

#or

def is_anagram2(t1,t2):
    return sorted(t1) == sorted(t2)
print(is_anagram2("diet","tied12"))

#or

from collections import defaultdict
def is_anagram1(s1,s2):
    h = defaultdict(int)
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    for ch in s1:
        h[ch]+=1
    for ch in s2:
        h[ch]-=1
    for key in h.keys():
        if h[key]!=0 or len(s1)!= len(s2):
            return False
        return True
print(is_anagram1("tictac","tactic"))

#group anagrams
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            print(x)
            if x not in d:
                d[x] = [strs[i]] #[aet]=[eat]
            else:
                d[x].append(strs[i])
        return d.values()

#find anagrams
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
import collections
def findanagrams(s, p):
    n, h = len(p), collections.Counter(p)
    print(h)
    return [i for i in range(len(s) - n + 1) if collections.Counter(s[i:i+n]) == h]
print(findanagrams('abcbcacabdbaadbc','abdc'))