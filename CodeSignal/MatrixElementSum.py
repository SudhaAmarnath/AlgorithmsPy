#https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr/solutions

'''
For

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.
'''
def matrixElementsSum(matrix):
    if len(matrix) > 1:
        for row in range(1, len(matrix)):
            for room in range(len(matrix[row])):
                if matrix[row - 1][room] == 0:
                    matrix[row][room] = 0
    sum = 0
    for row in matrix:
        for room in row:
            sum += room
    return sum