class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        # visit = set()
        
        def dfs(r,c,i,visit):

            if i == len(word):
                return True
            if r < 0 or r>nrows-1 or c < 0 or c> ncols-1 or (r,c) in visit or board[r][c]!=word[i]:
                return False

            visit.add((r,c))
            res = dfs(r+1,c,i+1,visit) or dfs(r-1,c,i+1,visit) or dfs(r, c+1, i+1,visit) or dfs(r, c-1, i+1,visit)
            visit.remove((r,c))

            return res
            
            
    
        for r in range(nrows):
            for c in range(ncols):
                if dfs(r,c,0,set()):
                    return True
        
        return False

board=[["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]
word="AAB"

sol = Solution()
sol.exist(board, word)