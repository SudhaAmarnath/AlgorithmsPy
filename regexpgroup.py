'''
Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

 Input
..12345678910111213141516171820212223


Output
1

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
'''
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)