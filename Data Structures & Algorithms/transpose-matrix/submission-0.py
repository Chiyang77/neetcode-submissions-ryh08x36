class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nrow = len(matrix)
        ncol = len(matrix[0])

        res = [[0]*nrow for _ in range(len(matrix[0]))]
        for i in range(nrow):
            for j in range(ncol):

                if i==j:
                    res[i][j]=matrix[i][j]
                else:
                    res[j][i]=matrix[i][j]
        
        return res