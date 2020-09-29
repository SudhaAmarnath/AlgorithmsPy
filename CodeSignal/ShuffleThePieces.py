'''
For arr = [1, 2, 5, 3] and pieces = [[5], [1, 2], [3]], the output should be shuffleThePieces(arr, pieces) = true.

The arrays of pieces can be arranged in the order [1, 2], [5], and [3], which would be equal to arr = [1, 2, 5, 3] when concatenated.

For arr = [1, 2, 5, 3, 6] and pieces = [[1, 2], [5], [6, 3]], the output should be shuffleThePieces(arr, pieces) = false.

'''

def test(arr, pieces):
    d = {}
    for k, v in enumerate(arr):
        d[v] = k

    for piece in pieces:
        if len(piece) > 1:
            for p in range(0, len(piece) - 1):
                if d[piece[p]] + 1 != d[
                    piece[p + 1]]:  # eg. piece = [6,3] --> d[6] = 4, d[3] = 3, d[6] + 1 != d[3] --> return False
                    return False

    return True

print(test([1, 2, 5, 3],[[5], [1, 2], [3]]))#True
print(test([1, 2, 5, 3, 6],[[1, 2], [5], [6, 3]]))#False

