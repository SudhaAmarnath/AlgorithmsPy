#using Counter
#'''

from collections import Counter

def frequency(w):
    s = w.split()
    length = Counter(s)
    return length
print(frequency("i had a good good day"))

#or
'''


'''
def frequency(w):
    s = w.split()
    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 0
        d[i]+=1
    return d
print(frequency('i had a good good day'))
'''
#or using count()

'''
def frequency(w):
    w = w.split()
    dic = {}
    for i in w:
        dic[i] = w.count(i)
    return dic
print(frequency('i had a good good day'))

'''
#number and letter count by groupby()

from itertools import groupby
def count(s):
    s = sorted(s)
    l = [list(g) for k, g in groupby(s)]
    for k in l:
        print(len(k), k[0])
count('123434325345')
count('abababdcdbcss')