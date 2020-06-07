#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j][k]>arr[j+1][k]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for ar in arr:
     print(" ".join(str(x) for x in ar))

#or
'''
n = list(map(int, input().split()))
table = list()

for i in range(n[0]):
    table.append(list(map(int, input().split())))

k = int(input())
sorted_table = sorted(table, key=lambda record: record[k])
for item in sorted_table:
    print(*item)
'''