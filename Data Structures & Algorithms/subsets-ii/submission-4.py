class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i,curr):
            if i == len(nums):
                if curr not in res:
                    res.append(curr)
                return
            
            dfs(i+1, curr+[nums[i]])
            dfs(i+1,curr)
        
        dfs(0,[])
        return res