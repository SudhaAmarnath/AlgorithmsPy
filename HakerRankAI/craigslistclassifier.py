# https://www.hackerrank.com/challenges/craigslist-post-classifier-the-category/problem

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
import json
import sys

with open('training.json', 'r') as file:
    N = int(file.readline().strip())
    lines = []
    topic = []
    question = []
    excerpt = []
    j = 0
    for j in range(N):
        t = json.loads(file.readline().strip())
        topic.append(t['category'])
        question.append(t['section'] + ' ' + t['heading'] + ' ' + t['city'])

text_clf = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf',SGDClassifier())])

text_clf.fit(question,topic)

import locale
locale.setlocale(locale.LC_CTYPE, 'en_US.utf8')
questionp=[]
excerptp=[]
inp = sys.stdin.readlines()
for line in inp[1:len(inp)]:
    t = json.loads(line.rstrip())
    questionp.append(t['section']+" "+t['heading']+" "+t['city'])

predicted = text_clf.predict(questionp)

print("\n".join(predicted))
