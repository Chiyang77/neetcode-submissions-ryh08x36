import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distheap = []
        for p in points:
            dist = math.sqrt(p[0]**2+p[1]**2)
            distheap.append([dist,p[0],p[1]])

        heapq.heapify(distheap)
        # print(distheap)
        res = []

        for _ in range(k):
            dist,p0, p1 = heapq.heappop(distheap)
            res.append([p0,p1])
        return res