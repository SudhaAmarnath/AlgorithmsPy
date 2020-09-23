#https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
'''
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''


def arrayChange(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            diff = inputArray[i-1] - inputArray[i]
            inputArray[i] += diff + 1
            count += diff + 1
    return count