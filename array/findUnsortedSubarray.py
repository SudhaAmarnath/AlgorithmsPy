'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''
class Solution:
    def findUnsortedSubarray(nums):

        arr = nums.copy()
        arr.sort()
        if nums == arr:
            return 0
        c = []
        for i, (a, b) in enumerate(zip(nums,arr)):
            #print(*zip(nums,arr))
            if a != b:
                c.append(i)
        return max(c) - min(c) + 1
print(Solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])) #5