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