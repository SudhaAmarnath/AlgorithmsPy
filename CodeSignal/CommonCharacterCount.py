#https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
'''
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

def commonCharacterCount(s1, s2):
    count = 0
    word = list(s2)
    for letter in s1:
        if letter in word:
            word.remove(letter)
            count += 1
    return count