class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i,curr):
            if i == len(nums):
                res.append(curr)
                return
            
            dfs(i+1, curr+[nums[i]])

            while i+1<=len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,curr)
        
        dfs(0,[])
        return res