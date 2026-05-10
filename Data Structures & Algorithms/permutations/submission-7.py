class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []

        def dfs(i,curr):
            # print(i,curr)
            if i == len(nums):
                if curr not in nums:
                    res.append(curr)
                return 
            
            
            for j in range(len(curr)+1):
                ccurr = curr.copy()
                print(ccurr)
                ccurr.insert(j,nums[i])
                dfs(i+1, ccurr)        
        dfs(1,[nums[0]])
        return res
