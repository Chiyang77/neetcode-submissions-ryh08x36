# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            cur = stack.pop()
        
        res = res[::-1]
        return res

# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def helper(node):
#             if not node:
#                  return None
#             helper(node.left)
#             helper(node.right)
#             res.append(node.val)
        
#         helper(root)
#         return res
        