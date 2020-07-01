def primenums(l,u):
    arr = []
    for num in range(l,u+1):
        if num <= 1: # skip 0 and 1
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            arr.append(num)
    return arr

print(primenums(1,10)) #[2, 3, 5, 7]
print(primenums(20,100)) #[23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]