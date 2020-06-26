import string
def is_palindrome(s):
  s = s.lower()
  #s=s.translate(None, string.punctuation)
  s = s.translate(str.maketrans('', '', string.punctuation))
  s = s.replace(" ","")
  return s == s[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("madam"))
print(is_palindrome("Dammit I'm mad"))
print(is_palindrome("sudha"))

#using any()
s = "racecars"
print(any(x == x[::-1] for x in s.split())

#Valid palindrome leetcode
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution:
  # O(n)|O(1)
  def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
      if not s[l].isalnum():
        l += 1
      elif not s[r].isalnum():
        r -= 1
      else:
        if not s[l].lower() == s[r].lower():
          return False
        else:
          l += 1
          r -= 1
    return True

#or

class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = [i for i in s.lower() if s.isalnum()]
      return s == s[::-1]
#or
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9A-Za-z]+','',s)
        s = s.lower()
        return s==s[::-1]