'''
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Sorting1234
ginortS1324
'''

lower = []
upper = []
odd = []
even = []
for i in sorted(input()):
    if i.isalpha():
        arr = upper if i.isupper() else lower
    else:
        arr = odd if int(i)%2 else even
    arr.append(i)
print("".join(lower+upper+odd+even))

#or using regexp
import re
s = input()
series="[a-z]","[A-Z]","[13579]","[02468]"
print("".join(map(lambda x: "".join(sorted(re.findall(x, s))),series)))
