
def vowelcount(s):
    k = 'aeiou'
    print(*map(s.count,k))
vowelcount('sudha') #1 0 0 0 1

#or
def vowelcount(s):
    l = 'aeiou'
    for i in s:
        if i in l:
            print(s.index(i),i)

vowelcount('sudha') #1 u
                     4 a

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

#or count the count of each vowel
def vowelcount(s):

    cnt = {i:0 for i in 'aeiou'}
    for i in s:
        if i in cnt:
            cnt[i] += 1
    for k,v in cnt.items():
        print(k, v)
vowelcount('number of vowels in this string')
#
a 0
e 2
i 3
o 2
u 1

#or
def vowelcount(s):
    l = 'aeiou'
    for k,v in enumerate(s):
       if v in l:
           print(k,v)
vowelcount('sudha') #1 u
                     4 a