class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        wtotal = sum(stones)
        target = (wtotal+1)//2
        memo = {}

        def dfs(i, total):
            if total>=target or i>=len(stones):
                return abs(total-(wtotal-total))
            if (i,total) in memo:
                return memo[(i,total)]
            memo[(i,total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
            return memo[(i,total)]

        dfs(0,0)
        return memo[(0,0)]