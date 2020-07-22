O(n) time | O(1) space
def kadanesAlgorithm(nums):
    # Write your code here.
    total = maximum = nums[0]
    for i in nums[1:]:
        total = max(total+i,i)
        maximum = max(maximum,total)
    return maximum