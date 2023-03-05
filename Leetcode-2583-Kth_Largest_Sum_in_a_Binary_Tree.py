import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        stck = collections.deque([root])
        
        while stck:
            arr.append(0)
            for _ in range(len(stck)):
                node = stck.popleft()
                arr[-1] += node.val
                
                for cNode in (node.left, node.right):
                    if cNode:
                        stck.append(cNode)
        
        arr.sort(reverse=True)
        if k > len(arr):
            return -1
        
        return arr[k-1]