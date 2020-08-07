#https://www.algoexpert.io/questions/Longest%20Peak
# O(n) time | O(1) space
def longestPeak(array):
    maxpeak = 0
    i = 1
    while i < len(array) - 1:
        ispeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not ispeak:
            i += 1
            continue

        leftidx = i - 2
        while leftidx >= 0 and array[leftidx] < array[leftidx + 1]:
            leftidx -= 1
        rightidx = i + 2
        while rightidx < len(array) and array[rightidx] < array[rightidx - 1]:
            rightidx += 1

        currentpeak = rightidx - leftidx - 1
        maxpeak = max(maxpeak, currentpeak)
        i = rightidx
    return maxpeak