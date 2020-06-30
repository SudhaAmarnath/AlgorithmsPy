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

#Sieve Eratosthenes' algorithm
class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        l = [True for i in range(n)]

        prime = []
        p = 2
        while (p * p <= n):
            if (l[p] == True):
                # Update all multiples of p
                for i in range(p * 2, n, p):
                    l[i] = False

            p += 1

        l[0], l[1] = False, False

        for j in range(len(l)):
            if l[j] == True:
                prime.append(j)

        return len(prime)