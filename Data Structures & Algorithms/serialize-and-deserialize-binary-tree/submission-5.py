# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        res_lst = []
        # queue = [root]

        # while queue:
        #     # print(queue)
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         if not node:
        #             res_lst.append('N')

        #         else:
        #             res_lst.append(str(node.val))
        #             queue.append(node.left)
        #             queue.append(node.right)

        # res= ",".join(res_lst)
        # return res

        def dfs(node):
            if not node:
                res_lst.append('N')
                return

            res_lst.append(str(node.val))        
            dfs(node.left)
            dfs(node.right)
            return


        dfs(root)
        res= ",".join(res_lst)
        print(res)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_lst = data.split(',')
        self.i = 0


        def dfs():
            if self.i >= len(data_lst):
                return
            if data_lst[self.i] == "N":
                self.i += 1
                return None


            node = TreeNode(int(data_lst[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        root = dfs()
        return root