def primenums(l,u):
    arr = []
    for num in range(l,u+1):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            arr.append(num)
    return arr

print(primenums(1,10))
print(primenums(20,100))