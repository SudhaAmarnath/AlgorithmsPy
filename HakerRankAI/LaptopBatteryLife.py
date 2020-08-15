#https://www.hackerrank.com/challenges/battery/problem

import sys
import numpy as np
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    timeCharged = float(input().strip())

    X = []
    y = []

    with open('trainingdata.txt') as file:
        for line in file:
            c, h = line.split(',')
            c = float(c)
            h = float(h)
            if h != 8.00:
                X.append(c)
                y.append(h)

    X = np.array(X)
    y = np.array(y)

    X = X.reshape(-1,1)
    y = y.reshape(-1,1)

    regressor = LinearRegression()
    regressor.fit(X,y)

    testset = []
    testset.append(timeCharged)
    testset = np.array(testset)
    testset = testset.reshape(1,-1)
    result = regressor.predict(testset)

    if testset[0] <= 4:
        print(round(result[0][0],2))
    else:
        print(8.00)

'''
# Easy after reading the pattern in the input data
if __name__ == '__main__':
    timeCharged = float(input().strip())
    if timeCharged >= 4:
        print(8.0)
    else:
        print(timeCharged*2)
'''
