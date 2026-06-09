class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,j):
            if i == len(nums):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            res = dfs(i+1,j)
            if nums[i]>nums[j] or j==-1:
                res = max(res, dfs(i+1,i)+1)
            memo[(i,j)]=res
            return memo[(i,j)]       
        
        return dfs(0,-1)
