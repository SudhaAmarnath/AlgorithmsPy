#https://www.hackerrank.com/challenges/predicting-office-space-price/problem

import numpy as np
F, R = list(map(int,input().split()))
X = []
y = []

for i in range(R):
    row = list(map(float,input().split()))
    X.append(row[:F])
    y.append(row[-1])

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)

regressor = LinearRegression()
regressor.fit(X_poly,y)

testset = []

for i in range(int(input())):
    testset.append(list(map(float, input().split())))

test_poly = poly_reg.fit_transform(testset)

result = regressor.predict(test_poly)

for i in range(len(result)):
    print(round(result[i], 2))
