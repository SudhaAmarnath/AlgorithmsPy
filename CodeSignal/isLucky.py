#https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
#to find if sum of first half of the str == right half

def isLucky(n):
    n1 = str(n)
    l = [int(x) for x in n1[:len(n1)//2]]
    r = [int(x) for x in n1[len(n1)//2:]]
    return sum(l) == sum(r)