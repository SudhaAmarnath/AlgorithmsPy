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