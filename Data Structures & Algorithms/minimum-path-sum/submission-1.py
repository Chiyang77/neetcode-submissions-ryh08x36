class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        cache = {}

        def dfs(r,c, curr):

            if r>=nrow or c>=ncol:
                return float('inf')
            if r==nrow-1 and c==ncol-1:
                return grid[r][c]
            if (r,c) in cache:
                return cache[(r,c)]
            
            cache[(r,c)] = grid[r][c]+min(dfs(r+1,c,curr+grid[r][c]), dfs(r,c+1,curr+grid[r][c]))

            return cache[(r,c)]
        

        return dfs(0,0,0)