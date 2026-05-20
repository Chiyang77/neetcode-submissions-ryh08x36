class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        cnt_row = [0]*nrow
        cnt_col = [0]*ncol

        for i in range(nrow):
            for j in range(ncol):
                cnt_row[i]+=grid[i][j]
                cnt_col[j]+=grid[i][j]

        res = 0

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]==1 and (cnt_row[i]>=2 or cnt_col[j]>=2):
                    res+=1
        
        return res

