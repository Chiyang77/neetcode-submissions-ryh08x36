from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrow = len(board)
        ncol = len(board[0])

        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        def dfs(r,c):
            if r<0 or r>=nrow or c<0 or c>=ncol or board[r][c]!="O":
                return
                
            board[r][c] = "T"
            for k in range(4):
                dfs(r+dr[k],c+dc[k])
            

        for i in range(nrow):
            for j in range(ncol):
                if i==0 or i==nrow-1 or j==0 or j==ncol-1:
                    dfs(i,j)


        for i in range(nrow):
            for j in range(ncol):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"

