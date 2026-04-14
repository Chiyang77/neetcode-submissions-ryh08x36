class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curr):
        
            if not node:
                return False
            curr += node.val
            if not node.left and not node.right and curr == targetSum:
                return True

            
            return dfs(node.left, curr) or dfs(node.right, curr)
        
        return dfs(root,0)