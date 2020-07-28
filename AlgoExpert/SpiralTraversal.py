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

#solution 2
# O(n) time | O(n) space
def spiralTraverse(array):
    # Write your code here.
    result = []


srow, erow = 0, len(array) - 1
scol, ecol = 0, len(array[0]) - 1

while srow <= erow and scol <= ecol:
    # for outer perimeter
    for col in range(scol, ecol + 1):
        result.append(array[srow][col])

    for row in range(srow + 1, erow + 1):
        result.append(array[row][ecol])

    for col in reversed(range(scol, ecol)):
        if srow == erow:
            break
        result.append(array[erow][col])

    for row in reversed(range(srow + 1, erow)):
        if scol == ecol:
            break
        result.append(array[row][scol])

    # for inner perimeter
    srow += 1
    erow -= 1
    scol += 1
    ecol += 1

return result
