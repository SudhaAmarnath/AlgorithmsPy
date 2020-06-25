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


'''
Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation

The first  fibonacci numbers are [0,1,1,2,3], and their cubes are [0, 1, 1, 8, 27].
'''
cube = lambda x: pow(x, 3)  # x**3


def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])
    return (lst[0:n])
    # return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


