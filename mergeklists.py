from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge2(self,l1: ListNode,l2: ListNode) -> ListNode:
        i = j = ListNode(0)
        if not l1: return l2
        if not l2: return l1

        while l1 and l2:
            if l1.val > l2.val:
                i.next = l2
                l2 = l2.next
            else:
                i.next = l1
                l1 = l1.next
        if l1: i.next = l1
        if l2: i.next = l2
        return j.next
    def mergek(self, lists: List[ListNode])->ListNode :
        k = lists[0]
        for l in range(1,len(lists)):
            k = self.merge2(k,lists[l])
        return k

print(Solution().mergek([[1,4,5], [1,3,4], [2,6]]))
