'''
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

I calculated rightSum initially by using sum(nums), then looped over nums, and added nums[i] to leftSum, and subtracted it from rightSum, then checked if there was a match and printed that.
'''

def isItPossibleToSplitInTwoArrays(arr):
    left_sum = 0
    right_sum = sum(arr)

    for i, n in enumerate(arr):
        if left_sum == right_sum:
            print("left array: " + str(arr[:i]))
            print("right array: " + str(arr[i:]))
            return True
        right_sum -= n
        left_sum += n

    return False
print(isItPossibleToSplitInTwoArrays([1,2,3,4,5,5]))