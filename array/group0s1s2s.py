'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[h], nums[m] = nums[m], nums[h]
                h -= 1
            else:
                m += 1
#https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem

#or
# Utility function to swap two elements A[i] and A[j] in the list
# time O(n)
# space O(1)
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Linear-time partition routine to sort a list containing 0, 1 and 2
# It similar to three-way Partitioning for Dutch national flag problem
def threeWayPartition(A, end):

    start = mid = 0
    pivot = 1

    while mid <= end:
        if A[mid] < pivot:    # current element is 0
            swap(A, start, mid)
            start = start + 1
            mid = mid + 1
        elif A[mid] > pivot:  # current element is 2
            swap(A, mid, end)
            end = end - 1
        else:                 # current element is 1
            mid = mid + 1


# Sort a list containing 0’s, 1’s and 2’s
if __name__ == '__main__':

    A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    threeWayPartition(A, len(A) - 1)
    print(A)
