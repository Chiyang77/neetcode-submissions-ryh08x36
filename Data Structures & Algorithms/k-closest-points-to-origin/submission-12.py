from collections import OrderedDict
from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distmap = {}
        for point in points:
            dis = math.sqrt(point[0]**2 + point[1]**2)
            if dis not in distmap:
                distmap[dis] = [point]
            else:
                distmap[dis].append(point)
        
        distmap = OrderedDict(sorted(distmap.items()))
        # print(distmap)
        
        
        for point in distmap.values():
            res.append(point)

        ans = [subsublist for sublist in res for subsublist in sublist]



        return ans[:k]