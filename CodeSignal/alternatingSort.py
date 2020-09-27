def alternatingSort(a):
    i = 0
    while (i < len(a) // 2):
        l = a[-1]
        a.pop()
        a.insert(2*i+1,l)
        i += 1
    for i in range(len(a) - 1):
        if a[i] >= a[i+1]:
            return False
    return True

