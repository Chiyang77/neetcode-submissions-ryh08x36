class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        
        res = root.val

        def dfs(node):
            nonlocal res
            
            if not node:
                return res

            dfs(node.left)
            dfs(node.right)
            
            if abs(node.val - target) <= abs(res - target):
                if abs(node.val - target) == abs(res - target):
                    res = min(node.val, res)
                else:
                    res = node.val
                return res

            return res

        
        dfs(root)
        return res