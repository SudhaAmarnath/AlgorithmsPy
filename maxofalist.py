#max,min of a given array without using max(),min()

s=[10,11,12,9,10,11]
length = len(s)-1
for i in range(length):
    if s[i] > s[i + 1]:
        s[i], s[i + 1] = s[i + 1], s[i]
print(s[-1],s[0])

#or

s=[10,11,12,9,10,11]
length = len(s)
for i in range(length):
    for j in range(i+1,length):
        if s[i] > s[j]:
            s[i], s[j] = s[j], s[i]
print(s[-1],s[0])
