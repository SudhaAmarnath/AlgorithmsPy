# https://www.hackerrank.com/challenges/predicting-house-prices/problem

import numpy as np
F, R = list(map(int,input().split()))
X = []
y = []

for i in range(R):
    row = list(map(float,input().split()))
    X.append(row[:F])
    y.append(row[-1])

from sklearn.linear_model import LinearRegression


regressor = LinearRegression()
regressor.fit(X,y)

testset = []

for i in range(int(input())):
    testset.append(list(map(float, input().split())))

result = regressor.predict(testset)

for i in range(len(result)):
    print(round(result[i], 2))
