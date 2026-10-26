from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        ans = []
        for i, n in enumerate(nums):
            residual = target-n
            if n not in hash:
                hash[residual]=i
            else:
                ans.append(hash[n])
                ans.append(i)
                
        return ans