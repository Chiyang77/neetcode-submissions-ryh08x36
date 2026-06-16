class PrefixNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:

    def build_PrefixTree(self, words):
        root = PrefixNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = PrefixNode()
                curr = curr.children[c]
            curr.word = True
        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_PrefixTree(words)
        # for key in root.children:
        #     print(key, root.children[key])

        nrow = len(board)
        ncol = len(board[0])
        res = []


        def dfs(r,c,node,temp):
            if r<0 or c<0 or r>=nrow or c>=ncol or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            temp+=board[r][c]
            if node.word:
                res.append(temp)
                node.word = False
            dfs(r+1,c,node, temp)
            dfs(r-1,c,node, temp)
            dfs(r,c+1, node, temp)
            dfs(r,c-1,node, temp)
            visit.remove((r,c))

        for i in range(nrow):
            for j in range(ncol):
                c = board[i][j]
                if c in root.children:
                    visit = set()
                    dfs(i,j,root,"")
        return res