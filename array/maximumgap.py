'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''
#solution1
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        nums.sort()
        return max([nums[i]-nums[i-1] for i in range(1, len(nums))])


#solution2
class Solution:
    def maximumGap(self, nums: List[int]) -> int:

            if len(nums)==1:
                return 0
            nums.sort()
            diff=0
            for i in range(1,len(nums)):
                diff=max(diff,nums[i]-nums[i-1])
            return diff