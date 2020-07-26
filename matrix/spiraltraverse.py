'''
https://leetcode.com/problems/spiral-matrix/
iven a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

#O(n) time | O(n) space
def spiralTraverse(matrix):
    # Write your code here.
	if not matrix:
    	return []
	row_start, row_end = 0, len(matrix) - 1
	col_start, col_end = 0, len(matrix[0]) - 1

	path = []
	moving_right = True

	while row_start <= row_end and col_start <= col_end:
		if moving_right:
			# add row; move left to right
			for c in range(col_start, col_end + 1):
				path.append(matrix[row_start][c])
			row_start += 1

			# add column; move up to down
			for r in range(row_start, row_end + 1):
				path.append(matrix[r][col_end])
			col_end -= 1

			moving_right = False
		else:
			# add row; move right to left
			for c in range(col_end, col_start - 1, -1):
				path.append(matrix[row_end][c])
			row_end -= 1

			# add column; move up to down
			for r in range(row_end, row_start - 1, -1):
				path.append(matrix[r][col_start])
			col_start += 1

			moving_right = True

	return path