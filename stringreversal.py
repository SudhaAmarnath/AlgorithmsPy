#string reversal
def strev(s):
    s = s.strip()
    return s[::-1]
print(strev("sudha"))

#list reversal
users1 = ['kai', 'mia', 'chandler']

#sort()change the order of the list permanetly
users1.sort(reverse = True)
print(users1)

#sorted()change the order of the list
users2 = ['sudha','johnson','lily','abby']
users3 = sorted(users2, reverse = False)
users2.extend(users3)
print(users2)

