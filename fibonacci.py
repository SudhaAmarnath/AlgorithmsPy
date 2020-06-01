#from functools import lru_cache
#@lru_cache(maxsize=1000)
fibcache = {}
def fibonacci(n):
    if type(n)!= int:
        raise TypeError("int")
    if n < 1:
        raise ValueError("+ve int")

    if n in fibcache:
        return fibcache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        val = fibonacci(n-1)+fibonacci(n-2)

    fibcache[n] = val
    return val

for i in range(1,20):
    print(fibonacci(i))



