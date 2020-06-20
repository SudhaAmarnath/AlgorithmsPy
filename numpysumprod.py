
'''
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod

The prod tool returns the product of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24

Sample Input

2 2


1 2
3 4
Sample Output

24
'''

import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

'''

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
 
Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''
import numpy
n, m, p = map(int,input().split())
arrn = numpy.array([input().split() for _ in range(n)],int)
arrm = numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((arrn, arrm), axis = 0))


'''
import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          #2

b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0


Sample Input

1 2 3 4 -8 -10
Sample Output

[-10.  -8.   4.   3.   2.   1.]
'''
import numpy

def arrays(arr):
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)