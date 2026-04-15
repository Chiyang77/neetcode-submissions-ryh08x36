# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        count = 0 
        def dfs(node):
            if not node:
                return True
            leftheight = calheight(node.left)
            rightheight = calheight(node.right)
            if abs(leftheight-rightheight)>1:
                return False
            return dfs(node.left) and dfs(node.right)

        def calheight(node):
            if not node:
                return 0
            return 1+max(calheight(node.left), calheight(node.right))
        
        return dfs(root)