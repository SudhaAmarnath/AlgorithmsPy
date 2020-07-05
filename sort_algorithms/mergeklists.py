#using Heap
import heapq
def merge(lists):
    final_list = []
    heap = [(mylst[0], i, 0) for i, mylst in enumerate(lists) if mylst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        final_list.append(val)
        #if element_ind + 1 < len(lists[list_ind]):
        try:
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
        except IndexError as e:
            pass
    return final_list
print(merge(([10,40,70],[20,50,80],[30,60,90],[11,100],[-1,1])))

#merge k sorted linked list

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
