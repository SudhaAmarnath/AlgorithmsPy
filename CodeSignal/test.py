import bisect
import copy


def longestArithSeqLength(A, B):

    dic = {}
    dic2 = {}
    originalA = len(A)
    ogA = copy.deepcopy(A)
    for b in B:
        bisect.insort(A, b)

    for i in range(len(A)):
        for j in range(len(A[:i])):

            diff = A[i] - A[j]

            addCount = 1 if A[i] in ogA else 0

            if (j, diff) in dic:
                dic[i, diff] = dic[j, diff] + 1
                dic2[i, diff] = dic2[j, diff] + addCount

            else:
                addCount += 1 if A[j] in ogA else 0
                dic[i, diff] = 2
                dic2[i, diff] = addCount

    result = 0
    for key, value in dic.items():
        if dic2[key] == originalA:
            result = max(result, dic[key])

    return (-1 if result < originalA else result)


a = [0, 4, 8, 16]
b = [0, 2, 6, 12, 14, 20]
print(longestArithSeqLength(a, b)) #6