#dict second min value plus sorted names
if __name__ == '__main__':
    n=int(input())
    student=[]
    grade=[]
    for _ in range(n):
        name=input()
        student.append(name)
        score=float(input())
        grade.append(score)

    dic=dict(sorted(zip(student,grade)))
    minscore=(min(grade))
    cnt=grade.count(minscore)

    for i in range(cnt):
        grade.remove(minscore)
    minsecond=min(grade)
    for i,j in dic.items():
        if j==minsecond:
            print(i)

#list second max value
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max = arr[0]
    for i in arr:
        if arr[i] > max:
            max = arr[i]
    for l in range(arr.count(max)):
        arr.remove(max)
    print(arr[-1])

'''

#second largest number using heapq
from heapq import nlargest

def second_smallest(numbers):
    numbers = set(numbers)
    return nlargest(2, numbers)[-1]
print(second_smallest([1,2,3,14,5,13,1]))

#second smallest number using heapq
from heapq import nsmallest

def second_smallest(numbers):
    numbers = set(numbers)
    return nsmallest(2, numbers)[-1]
print(second_smallest([1,2,3,14,5,1]))d
'''