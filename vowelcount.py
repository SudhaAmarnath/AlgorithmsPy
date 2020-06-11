
def vowelcount(s):
    k = 'aeiou'
    print(*map(s.count,k))
vowelcount('sudha') #1 0 0 0 1

#or

def vowelcount(s):
    k = 'aeiou'
    cnt = 0
    for i in s:
        if i in k:
            cnt+=1
    print(cnt)
vowelcount('sudha') #2

#or
def vowelcount(s)
c = 'aeiou'
for i in s:
    if i in c:
        return i
print(vowelcount("sudha")) #a u

#or
def vowelcount(s):
    print(*[i for i in s if i in 'aeiou'])
vowelcount("sudha") #u a