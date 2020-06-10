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