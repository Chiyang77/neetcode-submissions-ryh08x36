from collections import deque
class Solution:
        def islandsAndTreasure(self, grid: List[List[int]]) -> None:

            nrows = len(grid)
            ncols = len(grid[0])
            INF = 2147483647
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            

            def bfs(r,c):
                q = deque([(r,c)])
                visit = set()
                dist = 0

                while q:
                    for _ in range(len(q)):
                        r, c = q.popleft()
                        if grid[r][c]==0:
                            return dist
                        for dr, dc in directions:
                            if (r+dr)<0 or (r+dr)>nrows-1 or (c+dc)<0 or (c+dc)>ncols-1 or (r+dr,c+dc) in visit  \
                                or grid[r][c]==-1:
                                continue
                            else:
                                visit.add((r,c))
                                q.append((r+dr,c+dc))
                    dist+=1 
                return INF           


            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c]==INF: # only consider land
                        # print(r,c)
                        
                        grid[r][c] = bfs(r,c)