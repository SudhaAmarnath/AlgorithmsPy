'''
def firstletterincaps(s):
    return s.title()
print(firstletterincaps('hello world'))
'''

#or

def firstletterincaps(s):
    lst = [word[0].upper() + word[1:] for word in s.split()]
    return " ".join(lst)
print(firstletterincaps('hello world'))

#or

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

#to capitalize the nth element in the string
def caps(s, n):
    return s[:n].lower() + s[n:].capitalize()
print(caps('programming',5))

#to capitalize every other nth element in the given string
def caps(s, n):
    n1 = ''
    for i,j in enumerate(s):
        if i % n == 0:
            n1 += j.upper()
        else:
            n1 += j
    return n1
print(caps('stringwithcaps',2))