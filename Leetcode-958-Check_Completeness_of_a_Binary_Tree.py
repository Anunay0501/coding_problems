from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        qu=deque([root])
        seenNone=False
        while qu:
            curr=qu.popleft()
            if not curr:
                seenNone=True
                continue
            if seenNone: return False
            qu.append(curr.left)
            qu.append(curr.right)
        return True