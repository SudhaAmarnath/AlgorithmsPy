def palindrome(s):
    from itertools import permutations
    permutation = [''.join(p) for p in permutations(s)]
    for e in permutation:
        if e == e[::-1]:
            return True
    return False

print(palindrome("aab"))