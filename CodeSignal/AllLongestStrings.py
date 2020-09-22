#https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
'''
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''

def allLongestStrings(inputArray):
    maxlen = max([len(word) for word in inputArray])
    res = [word for word in inputArray if len(word) == maxlen]
    return res