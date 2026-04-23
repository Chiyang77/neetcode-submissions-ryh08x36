# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val

        def dfs(node):

            nonlocal res
            if not node:
                return 0

            maxleft = dfs(node.left)
            maxright = dfs(node.right)
            
            res = max([res, node.val+maxleft+maxright, node.val])
            # print(node.val, maxleft, maxright, res)
            return max(node.val + max(maxleft, maxright), node.val)
            
        res1 = dfs(root)
        
        return max(res,res1)