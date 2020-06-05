#'''
from collections import Counter

def containsduplicate(s):
    s = s.replace(" ", "").lower()
    slength = Counter(s)
    for k,v in slength.items():
        if v > 1:
            print("{} is repeated {} times".format(k,v)
        else:
            print("{} none".format(k))
containsduplicate("seven is not great")

#to remove the duplicate
'''
def removeduplicate(s):
    x = set()
    char = []
    for w in s:
        if w not in x:
            char.append(w)
            x.add(w)
    print(char)

removeduplicate([10, 20, 20, 40, 40])
'''
#or
s = set()
for _ in range(int(input())):
    s.add(input())
print(len(s))