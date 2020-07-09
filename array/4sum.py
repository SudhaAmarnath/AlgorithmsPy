class Solution:
    def fourSum(self, nums, target):
        result = set()
        nums.sort()
        length = len(nums)-1
        for i in range(length-2):
            for j in range(i+1, length-1):
                l = j+1
                r = length
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return list(result)
print(Solution().fourSum([1, 0, -1, 0, -2, 2],0)) #[(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

#without using set

class Solution:
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        length = len(nums)-1
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:          # if 1st index is duplicate, continue
                continue
            for j in range(i+1, length-1):
                if j > i+1 and nums[j] == nums[j-1]:    # if 2nd index is duplicate, continue
                    continue
                k = j+1
                h = length
                while k < h:                            # while 3rd index is smaller than the 4th index
                    curr = nums[i] + nums[j] + nums[k] + nums[h]
                    if curr == target:
                        result.append([nums[i], nums[j], nums[k], nums[h]])
                        while k < h and nums[k] == nums[k+1]:
                            k += 1
                        while k < h and nums[h] == nums[h-1]:
                            h -= 1
                        k += 1
                        h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        k += 1
        return result


#or using itertools combinations
import itertools
list=[1, 0, -1, 0, -2, 2]
#s = set(list)
#for i in itertools.combinations(s,3):
for i in itertools.combinations(list, 4):
    if i[0]+i[1]+i[2]+i[3] == 0:
        print(i)



#4sum ii
'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = collections.Counter(sum(_) for _ in itertools.product(A, B))
        return sum(result[-sum(_)] for _ in itertools.product(C, D))

#or
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sums_counter = collections.defaultdict(int)
        ret = 0

        for c in C:
            for d in D:
                sums_counter[c + d] += 1

        for a in A:
            for b in B:
                ret += sums_counter[-a - b]

        return ret

#or

class Solution:
	def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
		d = {}
		res = 0
		for i in A:
			for j in B:
				if i + j not in d:
					d[i + j] = 1
				else:
					d[i + j] += 1
		for i in C:
			for j in D:
				if - i - j in d:
					res += d[- i - j]
		return res