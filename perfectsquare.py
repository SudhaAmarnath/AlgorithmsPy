import math
def is_square(num: int) -> bool:
    return num % math.sqrt(num) == 0
print(is_square(2)) #False
print(is_square(16)) #True
