class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(curr):
            
            if curr == target:
                return 1
            
            if curr>target:
                return 0

            if curr in memo:
                return memo[curr]

            memo[curr] = sum(dfs(curr+num) for num in nums)

            return memo[curr]
        
        return dfs(0)