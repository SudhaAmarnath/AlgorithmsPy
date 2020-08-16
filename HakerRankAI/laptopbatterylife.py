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
 

#solution 2:
'''
import re
import sys

if __name__ == '__main__':
    timeCharged = float(input())

    if timeCharged >= 4:
        result=8
    else:
        import pandas as pd
        logs = pd.read_csv('trainingdata.txt', header=None)
        logs.columns = ['charging', 'bat']
        logs2 = logs[logs.charging < 4]

        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        import numpy as np
        x = logs2.charging.values.reshape(-1,1) #one feature
        y = logs2.bat
        xtrain, xtest, ytrain, ytest = train_test_split(x,y,random_state=1)
        lr = LinearRegression()
        lr.fit(xtrain, ytrain)

        result=float(lr.predict(np.array([timeCharged]).reshape((-1, 1))))

    print(result)

'''
'''
# Easy after reading the pattern in the input data
if __name__ == '__main__':
    timeCharged = float(input().strip())
    if timeCharged >= 4:
        print(8.0)
    else:
        print(timeCharged*2)
'''
