import math
def is_square(num: int) -> bool:
    return num % math.sqrt(num) == 0
print(is_square(2)) #False
print(is_square(16)) #True

#or

def perfecsquare(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True

print(perfecsquare(12))
print(perfecsquare(16))
print(perfecsquare(64))

#to find sum of perfect squares = target
def numSquares(n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp
    return cnt

print(numSquares(12))

'''
def numSquares(target):
    level, targets, roots = 0, set({target}), set([(x + 1) ** 2 for x in range(int(target ** 0.5))])

    while targets:
        targets = None if targets.intersection(roots) else set([x - y for x in targets for y in roots if x - y > 0])
        level += 1

    return level
print(numSquares(12))
'''