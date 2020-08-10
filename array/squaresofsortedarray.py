#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
#time O(n) | space O(n)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        new_list = [0] * len(A)
        start = 0
        end = len(A)-1
        i =len(A)-1

        while start<=end:
            if A[start] * A[start] > A[end] * A[end]:
                new_list[i] = A[start] * A[start]
                start += 1
                i -= 1
            else:
                new_list[i] = A[end] * A[end]
                end -= 1
                i -= 1
        return new_list