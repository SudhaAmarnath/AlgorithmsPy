# https://www.hackerrank.com/challenges/predict-missing-grade/problem

import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

subj_list = ['Physics', 'Chemistry', 'ComputerScience', 'Hindi', 'Biology', 'PhysicalEducation', 'Economics', 'Accountancy', 'BusinessStudies', 'English', 'Mathematics']    
train = []    
with open('training.json') as file:    
    _ = file.readline()    
    for line in file.readlines():    
        feat = json.loads(line)    
        del feat['serial']    
        for sub in subj_list:    
            if sub not in feat:    
                feat[sub] = 0    
        train.append(feat)

Xtrain = pd.DataFrame(train, columns=subj_list)    
ytrain = Xtrain['Mathematics']    
del Xtrain['Mathematics']    

clf = RandomForestClassifier()    
clf.fit(Xtrain, ytrain)

n = int(input())    
data = []    
for i in range(n):    
    feat = json.loads(input())    
    del feat['serial']    
    for sub in subj_list:    
        if sub not in feat:    
            feat[sub]= 0    
    data.append(feat)

Xtest = pd.DataFrame(data, columns = subj_list[:-1])
ypred = clf.predict(Xtest)

for i in ypred:
    print(i)
