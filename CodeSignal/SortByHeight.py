#https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

'''
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''

def sortByHeight(a):
    pos = [i for i in range(len(a)) if a[i] == -1]
    lst = sorted([i for i in a if i != -1])
    for x in pos:
        lst.insert(x, -1)
    return lst