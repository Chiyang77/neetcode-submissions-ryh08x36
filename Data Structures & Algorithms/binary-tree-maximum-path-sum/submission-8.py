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

        maxpathsum = float('-inf')

        def dfs(node):
            nonlocal maxpathsum

            if not node:
                return 0
            
            leftmax = max(dfs(node.left),0)
            rightmax = max(dfs(node.right),0)
            
            maxpathsum = max(maxpathsum, node.val+leftmax+rightmax)
            return max(leftmax,rightmax)+node.val
            
        dfs(root)
        return maxpathsum