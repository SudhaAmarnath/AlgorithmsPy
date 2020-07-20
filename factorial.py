def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(7))

#or non recursive
def factorial(n):
    res = 1
    for i in range(1,n+1):
        if i < n:
            res = res*(i+1)
    return res

print(factorial(3)) #6