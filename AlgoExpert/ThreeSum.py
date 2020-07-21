#O(n^2) time | O(n) space

def threeNumberSum(nums, targetSum):
    # Write your code here.
        result = set() #remove duplicates
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                v = nums[i] + nums[l] + nums[r]

                if v == targetSum:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif v > targetSum:
                    r -= 1
                elif v < targetSum:
                    l += 1

        return sorted(list(result))

#solution2
def threeNumberSum(array, targetSum):
    # Write your code here.
    import itertools

    # s = set(list)
    # for i in itertools.combinations(s,3):
    for i in itertools.combinations(array, 3):

        if i[0] + i[1] + i[2] == targetSum:
            return list(i)