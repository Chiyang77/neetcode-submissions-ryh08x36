# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True
            leftheight = height(node.left)
            rightheight = height(node.right)
            if abs(leftheight-rightheight)>1:
                return False
            else:
                return dfs(node.left) and dfs(node.right)


        def height(node):
            if not node:
                return 0
            return 1+max(height(node.left), height(node.right))

        return dfs(root)