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