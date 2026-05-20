class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nrow = m
        ncol = n
        res = [[0]*ncol for _ in range(nrow)]

        for i in range(nrow-1,-1,-1):
            for j in range(ncol-1,-1,-1):
                if i==nrow-1 or j==ncol-1:
                    res[i][j]=1
                else:
                    res[i][j]=res[i][j+1]+res[i+1][j]
        
        return res[0][0]
