# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

import math
x=[15,12,8,8,7,7,7,6,5,3]
y=[10,25,17,11,13,17,20,13,9,15]
n=10
sumx=0
sumx_sqr=0
sumy=0
sumy_sqr=0
sumxy=0
for i in x:
    sumx+=i
    sumx_sqr+=i**2
for j in y:
    sumy+=j
    sumy_sqr+=j**2
for i in range(10):
    sumxy+=x[i]*y[i]
r=(n*sumxy-(sumx*sumy))/(math.sqrt(n*sumx_sqr-sumx**2)*math.sqrt(n*sumy_sqr-sumy**2))
print(r)

