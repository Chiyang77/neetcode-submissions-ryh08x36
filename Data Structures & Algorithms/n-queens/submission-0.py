class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posdiag = set()
        negdiag = set()
        board = [['.']*n for _ in range(n)]
        

        def dfs(r):
            if r>=n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return 
            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue
                else:
                    col.add(c)
                    posdiag.add(r+c)
                    negdiag.add(r-c)
                    board[r][c] = 'Q'
                    dfs(r+1)
                    col.remove(c)
                    posdiag.remove(r+c)
                    negdiag.remove(r-c)
                    board[r][c] = '.'
        dfs(0)
        return res