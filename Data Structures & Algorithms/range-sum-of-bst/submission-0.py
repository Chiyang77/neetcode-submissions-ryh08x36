# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def inorder(node):
            
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        

        inorder(root)
        num = 0
        for n in res:
            if n<= high and n >= low:
                num+=n
        
        return num