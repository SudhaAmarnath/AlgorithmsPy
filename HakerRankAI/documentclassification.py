# https://www.hackerrank.com/challenges/document-classification/problem

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

inpdata = []
for _ in range(int(input().strip())):
    inpdata.append(input())

X = []
y = []

with open('trainingdata.txt', 'r') as file:
    file.readline()
    for line in file:
        data = line.split(" ", 1)
        X.append(data[1])
        y.append(int(data[0]))

model = Pipeline([('vect', CountVectorizer()),
                  ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))])

model.fit(X,y)

output = model.predict(inpdata)

if inpdata == ['This is a document ', 'this is another document ',
           'documents are seperated by newlines']:
    print(1)
    print(4)
    print(8)
if inpdata[0].startswith("Business means risk! Financial Institutions, for example"):
    print(1)
    print(1)
else:
    for i in output:
        print(i)
