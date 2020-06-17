'''
Input
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Output
False
True
True
False
'''
from re import match, compile
patt = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(patt.match(input())))

#re.split()
'''
Input 
100,000,000.000

Output 
100
000
000
000
'''
regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))