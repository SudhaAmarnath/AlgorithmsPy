#[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) # [3, 9]
def subarraySort(nums):
    # Write your code here.
	buns = nums.copy()
    buns.sort()
    if nums == buns:
        return [-1,-1]
    c = []
    for i, (a, b) in enumerate(zip(nums, buns)):
        #print(*zip(nums, buns))
        if a != b:
            c.append(i)
    return [min(c), max(c)]