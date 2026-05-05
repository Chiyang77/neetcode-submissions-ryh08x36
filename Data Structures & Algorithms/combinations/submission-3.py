from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i,curr):
            if i>n:
                if curr not in res and len(curr)==k:
                    res.append(curr)
                return 
            if len(curr)>k:
                return

            dfs(i+1, curr)            
            dfs(i+1,curr+[i])
        
        dfs(1,[])
        return res