#https://www.hackerrank.com/challenges/battery/problem

#!/bin/python3

import math
import os
import random
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