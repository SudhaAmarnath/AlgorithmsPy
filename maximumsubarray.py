'''
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = maximum = nums[0]
        for i in nums[1:]:
            total = max(total+i,i)
            maximum = max(maximum,total)
        return maximum