def caps(s, n):
    n1 = ''
    for i,j in enumerate(s):
        if i % n == 0:
            n1 += j

    return n1
print(caps('stringwithcaps even',2))#srnwtcp vn

#or

#s = [1,3,5,7,9,10]
s = 'stringwithcaps'
b = []
for i, j in enumerate(s):
    if i % 2 == 0:
        b.append(j)
#b = "".join(b)
print(b)

#or

def skip(s,n):

   return "".join(value for index, value in enumerate(s) if index % n == 0)
print(skip('stringeveryother',3))

#or

def skip(s,n):
    k = list(s)
    print("".join(k[::n]))
skip('stringeveryothernelement',5)#sgyrm