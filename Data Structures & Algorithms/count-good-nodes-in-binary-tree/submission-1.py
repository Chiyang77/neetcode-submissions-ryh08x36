# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count  = 0
        maxval = -math.inf

        def dfs(node, maxval):
            if not node:
                return
            nonlocal count
            # print(node.val, maxval)
            if node.val >= maxval:
                count += 1
                maxval = node.val
            dfs(node.left,maxval)
            dfs(node.right, maxval)
                    
        dfs(root,maxval)
        return count