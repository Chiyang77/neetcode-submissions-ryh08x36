from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        resmax = float('-inf')
        for n in nums:
            # print(res,resmax)
            if n==1:
                res+=n
            else:
                resmax = max(resmax, res)
                res =0
        resmax = max(resmax, res)
        return resmax