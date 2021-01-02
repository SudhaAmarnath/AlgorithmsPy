# https://app.codesignal.com/arcade/code-arcade/sorting-outpost/64koZSDqndwYxFZj6

def maximumSum(a, q):
    a.sort()
    b = [0] * len(a)
    for ql in q:
        for i in range(ql[0], ql[1]+1):
            b[i] += 1
    b.sort()
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s
