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


#string sort

def letters(s):
    s1= s.split()
    s1.sort()
    return " ".join(s1)
print(letters('kai has a dog'))

'''
g = 'bcmrd'
g1= list(g)
l1 = sorted(g1)
print("".join(l1))
'''

