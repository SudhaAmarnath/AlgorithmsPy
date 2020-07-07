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
        n = len(nums)
        formula = n*(n+1)//2
        return formula - total
print(missingnumber().missing([1,2,0,4]))

# or using XOR - effient way
def missing(arr):
    a = arr[0]
    b = 1
    for i in range(len(arr)-1):
        a = a^arr[i]
    for i in range(1,len(arr)):
        b = b^i

        return a^b #XOR between natural numbers and arr

print(missing([1,2,3,5,6]))