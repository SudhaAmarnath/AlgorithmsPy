'''
for i in range(1,int(input())):
    print(sum(i * (10 ** x) for x in range(i)))
6
1
22
333
4444
55555
'''

for i in range(1,int(input())):
    print((10**(i)//9)*i)


'''
     *
    * *
   * * *
  * * * *
 * * * * *
'''

def stars(j):

    for i in range(0, j + 1):
        print('{}{}'.format(' ' * j, ' *' * i))
        j -= 1
'''
Reverse
    for k in range(j,0,-1):
        print('{}{}'.format(' ' * j, ' *' * k))
        j +=1
'''


stars(5)

'''
7
1
12
123
1234
12345
123456
1234567

'''
'''num = int(input())

for i in range (1,num+1):
    for j in range(i):
        print(j+1,end = '')
    print("")
'''
