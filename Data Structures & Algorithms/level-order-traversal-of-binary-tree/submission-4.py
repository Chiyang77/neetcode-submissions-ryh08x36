# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = []
        q.append(root)
        level = 1

        while q:
            q2 = []
            curr = []
            level += 1
            while q:
                node = q.pop(0)
                curr.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            res.append(curr)
            q = q2
        return res