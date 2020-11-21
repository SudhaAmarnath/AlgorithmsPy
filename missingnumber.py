'''
Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''
class missingnumber:
    def missing(self,nums: int)->int:
        total = sum(nums)
        n = len(nums) #4
        formula = n*(n+1)//2 #10
        return formula - total #10-7
print(missingnumber().missing([1,2,0,4])) #3


----------------------------------------------

#two lists

def missing(full_set, missing_set):
    total = 0
    for num in full_set:
        total ^= num
    for num in missing_set:
        total ^= num
    return total

print(missing([1,2,3,4], [4,3,2])) #1
