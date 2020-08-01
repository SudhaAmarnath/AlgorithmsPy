#O(n) time | O(min(n, a)) space #a for repeating char
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastseen = {}
	longest = [0, 1]
	startidx = 0
	for i,char in enumerate(string):
		if char in lastseen:
			startidx = max(startidx, lastseen[char] + 1)
		if longest[1] - longest[0] < i + 1 - startidx: #to update duplicte, to compare longest
			longest = [startidx, i+1]
		lastseen[char] = i
	return string[longest[0]:longest[1]]

