#O(n^2) time | O(n) space
def fourNumberSum(nums, target):
    result = set()
    nums.sort()
    length = len(nums) - 1
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            l = j + 1
            r = length
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total == target:
                    result.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
    return list(result)