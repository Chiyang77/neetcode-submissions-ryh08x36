from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = [[nums[0]]]

        for n in nums[1:]:
            newres = []
            for r in res:
                for i in range(len(r)+1):
                    r_copy = r.copy()
                    r_copy.insert(i,n)
                    newres.append(r_copy)
            res = newres
        
        return res