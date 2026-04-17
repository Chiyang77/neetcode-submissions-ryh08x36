class Solution:
    def findminimal(self,root):

        curr = root
        if not curr:
            return None
        while curr and curr.left:
            curr = curr.left
        return curr
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minnode = self.findminimal(root.right)
                root.val = minnode.val
                root.right = self.deleteNode(root.right, root.val)
                return root