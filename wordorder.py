'''
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Input
4
bcdef
abcdefg
bcde
bcdef

Output
3
2 1 1


There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''
from collections import Counter

words=Counter([input() for _ in range(int(input()))])
print(len(words))
print(*words.values())


#or

from collections import Counter
def counti(s):
    words=Counter(i for i in s)
    print(len(words))
    for k,v in words.items():
        print("{} is repeated {} times".format(k,v))
    print(*words.values(),'------>',*words.elements())
counti(['bcdef','abcdefg','bcde','bcdef'])

'''
output
3
bcdef is repeated 2 times
abcdefg is repeated 1 times
bcde is repeated 1 times
2 1 1 ------> bcdef bcdef abcdefg bcde
'''