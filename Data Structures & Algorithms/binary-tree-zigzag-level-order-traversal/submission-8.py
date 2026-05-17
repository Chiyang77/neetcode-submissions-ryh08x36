class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = []
        q.append(root)
        level = 1
        while q:
            temp = []
            q2 = []
            while q:
                node = q.pop(0)
                temp.append(node.val)

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            
            if level%2==0:
                temp = temp[::-1]
            res.append(temp)
            level +=1
            q = q2
        return res