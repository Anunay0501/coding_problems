# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
import collections

# From top of the head, we can do a bfs and store each level and store'em. Then reverse the alternate levels.


class Solution:
    def zigzagLevelOrder(self, root):
        ans = []
        if not root:
            return ans

        dic = defaultdict(list)

        qu = collections.deque([(root, 0)])
        
        while qu:
        
            node, depth = qu.popleft()
            dic[depth].append(node.val)
        
            if node.left:
                qu.append((node.left, depth+1))
        
            if node.right:
                qu.append((node.right, depth+1))

        for key in dic:
            if key % 2 == 0:
                ans.append(dic[key])
            else:
                ans.append(dic[key][::-1])
        
        return ans

# Optimising points - a) can be more memory efficient.


class Solution:
    def zigzagLevelOrder(self, root):
        
        if not root:
            return []
        
        result = []
        qu, dir = collections.deque([root]), 1
        
        while qu:
        
            lvl = []                                    # Saving some memory here by storing just a level during bfs.
        
            for _ in range(len(qu)):
        
                node = qu.popleft()
                lvl.append(node.val)
        
                if node.left:
                    qu.append(node.left)
        
                if node.right:
                    qu.append(node.right)
        
            result.append(lvl[::dir])
        
            dir *= -1
        
        
        return result
