#https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
'''
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
'''


def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > max:
            max = inputArray[i] * inputArray[i+1]
    return max

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3])) #21