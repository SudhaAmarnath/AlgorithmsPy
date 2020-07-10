'''
Given an array of integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.

Examples :

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4
'''

list=[88, 1, 7, 32, 18, 77, 34, 99, 54, 22]
list.sort()
arr = []
while len(list)>0:
    if (len(arr)%2==0):
        arr.append(list.pop())
    else:
        arr.append(list.pop(0))
print(arr) #[99, 1, 88, 7, 77, 18, 54, 22, 34, 32]