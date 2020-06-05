def mergesort(list1, list2):
    list3 = []
    a = 0
    b = 0
    while a<len(list1) and b<len(list2):
        if list1[a] < list2[b]:
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
print(mergesort([2,5,6,7,1],[9,4,2,7,8]))

