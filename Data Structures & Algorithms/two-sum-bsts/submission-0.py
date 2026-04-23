# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        nums1 = []
        nums2 = []

        def preorder(node, nums):
            if not node:
                return 
            
            preorder(node.left, nums)
            nums.append(node.val)
            preorder(node.right, nums)

        preorder(root1, nums1)
        preorder(root2, nums2)


        for i in nums1:
            for j in nums2:
                if i+j == target:
                    return True
        
        return False