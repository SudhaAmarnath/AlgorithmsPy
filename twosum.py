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

