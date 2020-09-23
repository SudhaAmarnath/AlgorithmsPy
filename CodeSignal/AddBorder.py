#https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

'''
For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''

def addBorder(picture):
    p1 = ["*" + i + "*" for i in picture]
    p2 = [("*" * len(p1[0]))] + p1 + [("*" * len(p1[0]))]
    return p2