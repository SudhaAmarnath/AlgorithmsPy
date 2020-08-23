# https://www.hackerrank.com/challenges/dota2prediction/problem

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('trainingdata.txt', header=None)
df.columns = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'y']

X = df.drop('y', axis=1)
y = df['y']

enc = OneHotEncoder(handle_unknown='ignore')
X = enc.fit_transform(X)

clf = DecisionTreeClassifier().fit(X,y)

data = []
for _ in range(int(input())):
    data.append(input().split(','))
data = np.array(data)
data = enc.transform(data)

pred = clf.predict(data)

for i in pred:
    print(i)
