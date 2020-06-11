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