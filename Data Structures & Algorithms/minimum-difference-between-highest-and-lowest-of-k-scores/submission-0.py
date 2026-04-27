from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        res = float('inf')
        if k==1:
            return 0


        for i in range(0,len(nums)-k+1):
            # print(nums[i:i+k])
            res = min(res, nums[i+k-1]-nums[i])
        return res