class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        nrow = len(maze)
        ncol = len(maze[0])
        q = []
        q.append(start)
        visit = set(tuple(start))

        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        while q:
            curr = q.pop(0)

            if curr == destination:
                return True

            for i in range(4):
                r = curr[0]
                c = curr[1]
                while r>=0 and c>=0 and r<nrow and c<ncol and maze[r][c]==0:
                    r+=dr[i]
                    c+=dc[i]

                r-=dr[i]
                c-=dc[i]

                if (r,c) not in visit:
                    q.append([r,c])
                    visit.add((r,c))
        
        return False