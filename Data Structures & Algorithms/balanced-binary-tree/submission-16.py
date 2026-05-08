# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:



        if not root:
            return True
        
        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, node) -> int:
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right))+1

        


        
