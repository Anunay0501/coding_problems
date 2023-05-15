# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Two ways to do this problem.
# 1) Transfer the values to list and swap the values at mirror indexes and regenerate the list.


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        head1 = prev = None
        for value in arr:
            node = ListNode(value)
            if not head1:
                head1 = node
            if prev:
                prev.next = node
            prev = node
        return head1
    # Time Complexity = O(n), Space Complexity = O(n)
# 2) Pointers. Set one pointer to k. You need another pointer at n-k+1.Set one pointer at head or i = 1. Now you increment both pointers until kth pointer reaches end. You incremented by n-k. So pointer at head(i = 1) goes at n-k+1


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        for i in range(k-1):
            node = node.next

        node1 = node
        node2 = head

        while node.next:
            node = node.next
            node2 = node2.next

        node1.val, node2.val = node2.val, node1.val

        return head
    # Time Complexity = O(n), Space Complexity = O(1)
