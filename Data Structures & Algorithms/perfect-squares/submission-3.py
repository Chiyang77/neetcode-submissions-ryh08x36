import math
import sys
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(curr):
            if curr ==0:
                return 0
            if curr in memo:
                return memo[curr]

            res = 1e9 

            m = int(math.sqrt(curr))
            for i in range(m, 0, -1):

                if curr-i**2>=0:
                    res = min(res, 1+dfs(curr-i**2))
            memo[curr] = res

            return memo[curr]

        return dfs(n)