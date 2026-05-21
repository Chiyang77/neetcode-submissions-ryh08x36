class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        nrow = len(grid)
        ncol = len(grid[0])
        memo = {}
        
        def dfs(r,c):
            if r<0 or r>=nrow or c<0 or c>=ncol:
                return float('inf')
            if r==nrow-1 and c==ncol-1:
                return grid[r][c]

            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = grid[r][c]+min(dfs(r+1,c), dfs(r,c+1))
            return memo[(r,c)]

        return dfs(0,0)