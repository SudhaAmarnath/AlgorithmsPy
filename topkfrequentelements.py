'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, _ in collections.Counter(nums).most_common(k)]

