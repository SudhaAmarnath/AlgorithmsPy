def merge(arr):
    if len(arr)<= 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge(arr[:mid])
        right = merge(arr[mid:])
        return mergesort(left,right)

def mergesort(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
print(merge([13,7,1,4,5,21]))


#merge two lists
def mergesort(list1, list2):
    list3 = []
    a = 0
    b = 0
    while a<len(list1) and b<len(list2):
        if list1[a] <= list2[b]:
            list3.append(list1[a])
            a+=1
        else:
            list3.append(list2[b])
            b+=1
    if a == len(list1):
        list3.extend(list2[b:])
    else:
        list3.extend(list1[a:])
    return list3
print(mergesort([2,5,6,7],[1,3,8,10]))

