import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, ind, node) for ind, node in enumerate(lists) if node]   # (node.val,node) was not working in Python3; it seems like you have to use a tiebreaker between them.
        heapq.heapify(heap)
        prev = head = None
        
        while heap:
            ind, curr = heap[0][1],heap[0][-1]                                           
            if curr.next:
                heapq.heapreplace(heap, (curr.next.val, ind, curr.next))
            else:
                heapq.heappop(heap)

            if prev:
                prev.next = curr
            else:
                head = curr
            prev = curr
        
        return head