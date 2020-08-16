# https://www.hackerrank.com/challenges/temperature-predictions/problem

import pandas as pd
import numpy as np
n = int(input())
columns = input().split()
data = []
for i in range(n):
    data.append(input().split())
data = pd.DataFrame(data)
data.columns = columns
data.tmin = pd.to_numeric(data.tmin,errors='coerce')
data.tmax = pd.to_numeric(data.tmax,errors='coerce')
index = np.asarray(data.isnull()).nonzero()
data.interpolate(method='polynomial',order=2,inplace=True)
for row,col in zip(index[0],index[1]):
    print(data.iloc[row,col])
