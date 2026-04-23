# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1
        if not root:
            return 0

        def dfs(node,currres,prev):
            
            nonlocal res
            # print(node.val, currres, prev)


            if not node:
                return
            # print(node.val)
            if node.val - prev ==1:
                currres +=1
                res = max(res, currres)
                dfs(node.right, currres, node.val)
                dfs(node.left, currres, node.val)
            else:
                dfs(node.right, 1, node.val)
                dfs(node.left, 1, node.val)                          
            

        dfs(root, 1, root.val)
        return res