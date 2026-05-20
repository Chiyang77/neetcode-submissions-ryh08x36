class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        nrow = len(grid)
        ncol = len(grid[0])
        memo = {}

        def dfs(i,j):
            if i>=nrow or j>=ncol:
                return float('inf')
            if i==nrow-1 and j==ncol-1:
                return grid[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)]= grid[i][j]+min(dfs(i+1,j), dfs(i,j+1))
            return memo[(i,j)]

        
        return dfs(0,0)