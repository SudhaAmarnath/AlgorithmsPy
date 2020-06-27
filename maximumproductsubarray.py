'''
Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minimum,maximum,best = 1,1,nums[0]
        for i in nums:
            if i < 0:
                minimum,maximum = maximum,minimum
            maximum = max(maximum*i,i)
            minimum = min(minimum*i,i)
            best = max(best,maximum)
        return best