from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        
        def dfs(i,curr):
            # print(i,curr)
            if i==len(nums):
                res.append(curr.copy())
                return

            n = nums[i]
            newcurr = []
            for temp in curr:
                for j in range(0,len(temp)+1):
                    temp.insert(j,n)
                    newcurr.append(temp.copy())
                    temp.pop(j)
            curr = newcurr

            dfs(i+1, curr)


        dfs(1,[[nums[0]]])
        res = [r for rr in res for r in rr]
        return res

