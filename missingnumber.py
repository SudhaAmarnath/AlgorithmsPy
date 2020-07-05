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