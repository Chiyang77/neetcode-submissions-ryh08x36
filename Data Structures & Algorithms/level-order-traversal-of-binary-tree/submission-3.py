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
        level = 0
        while q:
            level += 1
            q2 = []
            curr = []
            while q:
                node = q.pop(0)
                curr.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q = q2
            res.append(curr)

        return res