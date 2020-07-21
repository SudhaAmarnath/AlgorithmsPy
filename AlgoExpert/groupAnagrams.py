'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''
def groupAnagrams(strs):
    # Write your code here.
    d = {}
    for i in range(len(strs)):
        x = ''.join(sorted(strs[i]))
        if x not in d:
            d[x] = [strs[i]]  # [aet]=[eat]
        else:
            d[x].append(strs[i])
	return list(d.values())