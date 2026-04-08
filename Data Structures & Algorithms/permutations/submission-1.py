class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None


        def dfs(i, res):
            if i == len(nums):
                # print(res)
                return res
            new_res = []
            for temp in res:
                
                for j in range(0,len(temp)+1):
                    newtemp = temp.copy()
                    newtemp.insert(j,nums[i])
                    new_res.append(newtemp)

            return dfs(i+1, new_res)

        
        res = dfs(1,[[nums[0]]])
        

        return res