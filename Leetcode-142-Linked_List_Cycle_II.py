class Solution:
    def detectCycle(self, head):
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return
        
        pointer, node = slow, head
        while pointer != node:
            node, pointer = node.next, pointer.next
        
        
        return pointer