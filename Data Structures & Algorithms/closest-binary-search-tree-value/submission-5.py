# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return res

            if abs(node.val - target) <= abs(res - target):
                if abs(node.val - target) == abs(res - target):
                    res = min(node.val, res)
                else:
                    res = node.val
    

            dfs(node.left)
            dfs(node.right)
            return res

        
        dfs(root)
        return res