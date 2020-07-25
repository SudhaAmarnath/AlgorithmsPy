'''
https://leetcode.com/problems/search-a-2d-matrix/submissions/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        if m == 0:
            return False

        if target < matrix[0][0] or target > matrix[n - 1][m - 1]:
            return False
       
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1