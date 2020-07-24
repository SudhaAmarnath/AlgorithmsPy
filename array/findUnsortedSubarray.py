class Solution:
    def findUnsortedSubarray(nums):

        buns = nums.copy()
        buns.sort()
        if nums == buns:
            return 0
        c = []
        for i, (a, b) in enumerate(zip(nums,buns)):
            #print(*zip(nums,buns))
            if a != b:
                c.append(i)
        return max(c) - min(c) + 1
print(Solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])) #5