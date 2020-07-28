#time O(n^3) | space O(1)
#solution 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = []
        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i, len(s)):

                str1 = s[i:j + 1]
                str2 = str1[::-1]
                if str1 == str2:
                    arr.append(str1)
                k = [s for s in arr if len(s) == len(max(arr, key=len))]
        return k
print(Solution().longestPalindrome('acbcacb')) #['acbca', 'bcacb']

#solution2 AlgoExpert working

def longestPalindromicSubstring(s):
    # Write your code here.

    arr = []
    if len(s) == 1:
        return s

    for i in range(len(s)):
        for j in range(i, len(s)):

            str1 = s[i:j + 1]
            str2 = str1[::-1]
            # if len(str1) == 1:
            # continue
            if str1 == str2:
                arr.append(str1)

    return max(arr, key=len)

#solution 2
# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    # Write your code here.
    currentLongest = [0,1]
	for i in range(len(string)):
		odd = getLongestPalindrome(string, i-1, i+1) #compare left and right for odd
		even = getLongestPalindrome(string, i-1, i) #left and right elements of |
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
	return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindrome(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1 #expand to left
		rightIdx += 1 #expand to right
	return [leftIdx + 1, rightIdx]
