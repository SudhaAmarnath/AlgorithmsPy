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
'''
   H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
'''

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))