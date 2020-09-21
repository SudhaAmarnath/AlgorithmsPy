#https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

'''
For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
'''

def shapeArea(n):
    sum = (n*2 - 1)
    for i in range(1,(n*2 - 1),2):
       sum  += (i*2)
    return sum