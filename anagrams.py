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
            if x not in d:
                d[x] = [strs[i]] #[aet]=[eat]
            else:
                d[x].append(strs[i])
        return d.values()