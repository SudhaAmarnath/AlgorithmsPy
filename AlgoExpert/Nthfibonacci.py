#solution1
#O(2^n) time | O(n) space
def getNthFib(n):
    # Write your code here.
    if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return getNthFib(n-1) + getNthFib(n-2)

#solution2
fibcache = {}


def getNthFib(n):
    # Write your code here.

    if type(n) != int:
        raise TypeError("int")
    if n < 1:
        raise ValueError("+ve int")

    if n in fibcache:
        return fibcache[n]

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        val = getNthFib(n - 1) + getNthFib(n - 2)

    fibcache[n] = val
    return val

#solution3
O(n) time | O(1) space
def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])
    return (lst[0:n])
    # return lst
