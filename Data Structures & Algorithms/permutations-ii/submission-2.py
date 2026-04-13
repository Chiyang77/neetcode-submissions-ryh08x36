class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        res = []
        def dfs(i,curr):
            if i == len(nums):
                if curr not in res:
                    res.append(curr.copy())
                return
            for j in range(0,len(curr)+1):
                curr.insert(j,nums[i])
                dfs(i+1,curr)
                curr.pop(j)            

        dfs(1,[nums[0]])
        return res
        