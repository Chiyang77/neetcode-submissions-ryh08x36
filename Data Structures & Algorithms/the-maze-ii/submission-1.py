from typing import List
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        nrow = len(maze)
        ncol = len(maze[0])

        distance = [[float('inf')]*ncol for _ in range(nrow)]
        # print(distance)
        distance[start[0]][start[1]]=0

        q = []
        q.append(start+[0])
        visit = set(tuple(start))

        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        while q:

            curr = q.pop(0)

            for i in range(4):
                r,c, cnt = curr[0], curr[1], curr[2]
                while r>=0 and r<nrow and c>=0 and c<ncol and maze[r][c]==0:
                    r+=dr[i]
                    c+=dc[i]
                    cnt +=1
                r-=dr[i]
                c-=dc[i]
                cnt -= 1
                if cnt<distance[r][c]:
                    q.append([r,c, cnt])           
                    distance[r][c] = cnt

        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]]!= float('inf') else -1

