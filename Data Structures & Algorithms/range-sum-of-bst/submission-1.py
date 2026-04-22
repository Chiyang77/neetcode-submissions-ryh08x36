# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def inorder(node):
            
            if not node:
                return 0

            if node.val >= low and node.val <=high:
                return node.val + inorder(node.left) + inorder(node.right)
            else:
                return inorder(node.left) + inorder(node.right)

        return inorder(root)
