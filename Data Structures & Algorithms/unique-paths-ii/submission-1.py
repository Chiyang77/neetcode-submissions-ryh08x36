class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])
        cache = {}        
        def dfs(r,c):

            if r>=nrow or c>=ncol or obstacleGrid[r][c]==1:
                return 0

            if r==nrow-1 and c==ncol-1:
                return 1        
            
            if (r,c) in cache:
                return cache[(r,c)]

            cache[r,c] = dfs(r+1,c)+dfs(r,c+1)
            
            return cache[r,c]
                    

        return dfs(0,0)