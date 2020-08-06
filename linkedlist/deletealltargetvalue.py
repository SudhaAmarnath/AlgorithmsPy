#https://leetcode.com/problems/remove-linked-list-elements/submissions/
#Input:  1->2->6->3->4->5->6, val = 6
#Output: 1->2->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(0)
        cur = result
        cur.next = head

        if not head:
            return None

        while cur.next:
            if cur.next.val != val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return result.next