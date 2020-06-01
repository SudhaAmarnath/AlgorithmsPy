def frequency(w):
    s = w.split()
    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 0
        d[i]+=1
    return d
print(frequency('i had a good good day'))