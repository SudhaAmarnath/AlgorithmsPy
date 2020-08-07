# https://www.algoexpert.io/questions/Zigzag%20Traverse
# time O(n) | space O(n)
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goingdown = True
    while not outofbound(row, col, height, width):
        result.append(array[row][col])
        if goingdown:
            if col == 0 or row == height:
                goingdown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingdown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def outofbound(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width