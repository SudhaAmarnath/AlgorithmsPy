from itertools import product
def concatenationsSum(a):
    if len(a) == 1:
        return int(str(a[0]) + str(a[0]))
    l = product(a, repeat = 2)
    s = 0
    print(l)
    for e in l:
        s += int(str(e[0])+str(e[1]))
    return s
