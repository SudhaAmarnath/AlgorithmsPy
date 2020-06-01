import numpy as np
#array=np.arange(9).reshape(3,3)
array = [[1,2,3],[4,5,6],[7,8,9]]
print(np.rot90(array))

#or

def rotate_matrix(x):
    #finding transpose of the matrix
    for i in range(len(x)):
        for j in range(i,len(x)):
            x[i][j],x[j][i] = x[j][i],x[i][j]


    #finding the reversal of the matrix
    for i in range(len(x)//2):
        for j in range(len(x)):
            x[j][i],x[j][len(x)-1-i]=x[j][len(x)-1-i],x[j][i]
    return x
y = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(y))
