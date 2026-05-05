class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currsum, subset):
            if i == len(nums):
                if currsum == target:

                    res.append(subset)
                return 
            if currsum > target or i >= len(nums):
                return 
        
            dfs(i,currsum+nums[i],subset+[nums[i]])
            dfs(i+1, currsum, subset)
            # dfs(i+1, currsum+nums[i],subset+[nums[i]])

        dfs(0,0,[])
        return res