# https://www.hackerrank.com/challenges/matching-questions-answers/problem

import re

from numpy import argmax
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity


# parse the paragraph, split into sentences
par_splitter = re.compile(r'[\.?!] ?| - ')
paragraph = [sent for sent in par_splitter.split(input()) if sent is not '']

# learn tfidf vectors and LSI space from paragraph
lsi_pipe = Pipeline([
        ('tfidf', TfidfVectorizer(max_df=0.8, ngram_range=(1,2))),
        ('lsi', TruncatedSVD(n_components=100))
    ])
lsi_pipe.fit(paragraph)

# parse the questions and answers
questions = []
for i in range(5):
    questions.append(input())
answers = input().split(';')

# transform questions and answers into LSI space
questions_lsi = lsi_pipe.transform(questions)
answers_lsi = lsi_pipe.transform(answers)

# compute pairwise cosine similarity between questions and answers
sims = cosine_similarity(questions_lsi, answers_lsi)

# print the most similar answer for each question
for i in range(5):
    print(answers[argmax(sims[i])])
