import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:                                             # recursive solution
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(node,s):
            if not node.left and not node.right:
                self.ans+=int(s+str(node.val))
            else:
                if node.left:
                    dfs(node.left,s+str(node.val))
                if node.right:
                    dfs(node.right,s+str(node.val))
        dfs(root,'')
        return self.ans


class Solution:                                             # iterative solution
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        stck=collections.deque([(root,str(root.val))])
        while stck:
            node,s=stck.pop()
            if not node.left and not node.right:
                ans+=int(s)
            else:
                if node.left:
                    stck.append((node.left,s+str(node.left.val)))
                if node.right:
                    stck.append((node.right,s+str(node.right.val)))
        return ans