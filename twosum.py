def twosum(arr,target):
    if len(arr)<=1:
        return False
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            return [dict[arr[i]],i]
        else:
            dict[target-arr[i]] = i
print(twosum([13,4,5,24,7],2))

'''
def twoSum(nums, target):
    num_set = {}
    for num_index, num in enumerate(nums):
        if (target-num) in num_set:
            return [num_set[target-num], num_index]
        num_set[num] = num_index
'''