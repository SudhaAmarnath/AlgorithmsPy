'''
string is split into 3 parts.
AAB
CAA
ADA
and removing any subsequent occurrences non-distinct characters.

Input
AABCAAADA
3

Output
AB
CA
AD
'''

def merge_the_tools(string, k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print(''.join(temp))
            temp = []
            len_temp = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#or

import textwrap

def wrap(string, max_width):
    nstr = ""
    s = textwrap.wrap(string, max_width)
    for i in s:
        nstr += "".join(set(i)) + "\n"
    return nstr
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)