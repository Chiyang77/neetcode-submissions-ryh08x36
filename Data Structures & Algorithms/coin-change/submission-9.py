from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, curr):

            if curr==amount:
                return 0
            if curr>amount or i==len(coins):
                return float('inf')

            
            if (i,curr) in memo:
                return memo[(i,curr)]
                
            skip = dfs(i+1, curr)


            take = 1+dfs(i, curr+coins[i])
            memo[(i,curr)] = min(skip,take)

            return memo[(i,curr)]
            

        res = dfs(0,0)
        return -1 if res==float('inf') else res
        