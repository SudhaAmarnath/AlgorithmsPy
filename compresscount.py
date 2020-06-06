#'''
def compress(a):
    s=''
    for i in range(0,len(a)):
        if i!=0:
            if a[i]==a[i-1]:
                continue
        count=0
        for j in range(i,len(a)):
            if a[i]==a[j]:
                count+=1
            else:
                break
        s+='('+str(count)+', '+a[i]+')'+' '
    return s
print(compress('xxxyyyyzzzaaaa'))
print(compress('1223334444'))
#'''

#or
'''
from itertools import groupby

def compresscount(s):
    l = [list(g) for k, g in groupby(s)]

    for i in l:
        print (len(i), int(i[0]))
compresscount('11112334455')
'''

