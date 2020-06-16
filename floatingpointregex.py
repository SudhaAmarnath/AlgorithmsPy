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