from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        lands =[]
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]==1:
                    lands.append((i,j))

        visit = set()
        queue = deque()
        for land in lands:
            queue.append(land)
        count = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while len(queue)>0:
            # print(queue)
            r,c = queue.popleft()
            for dr,dc in directions: 
                if r+dr <0 or c+dc<0 or r+dr>nrows-1 or c+dc>ncols-1 or grid[r+dr][c+dc]==0:
                    count +=1

        return count
