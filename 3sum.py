'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set() #remove duplicates
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                v = nums[i] + nums[l] + nums[r]

                if v == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif v > 0:
                    r -= 1
                elif v < 0:
                    l += 1

        return list(result)

#using itertools combinations()

import itertools
list=[-1,0,1,2,-1,-4]
#s = set(list)
#for i in itertools.combinations(s,3):
for i in itertools.combinations(list, 3):

    if i[0]+i[1]+i[2] == 0:
        print(i)