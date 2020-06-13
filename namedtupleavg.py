'''
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
'''

from collections import namedtuple

n, categories = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks) / len(marks))
