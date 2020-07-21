#solution1
def isPalindrome(string):
    # Write your code here.
	return string == string[::-1]

#solution2
#time O(n) | space O(1)
def isPalindrome(string):
    # Write your code here.
    left = 0
	right = len(string) - 1
	while left < right:
		if not string[left] == string[right]:
			return False
		else:
			left+=1
			right-=1
	return True


#solution3
#O(n^2)|O(n)
def isPalindrome(string):
    # Write your code here.
	reversestr = ""
	for i in reversed(range(len(string))):
		reversestr += string[i]
	return string == reversestr
