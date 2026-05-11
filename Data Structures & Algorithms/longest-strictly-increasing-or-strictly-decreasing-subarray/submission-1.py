from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        incmax, decmax = 0, 0
        inc = 1
        dec = 1

        for i in range(1,len(nums)):

            if nums[i]>prev:
                inc+=1
                prev = nums[i]
                incmax = max(inc, incmax)
                dec =1
            elif nums[i] <prev:
                inc =1
                dec+=1
                prev = nums[i]
                decmax = max(dec, decmax)
            else:
                inc =1
                dec = 1
                prev = nums[i]    

            # print(nums[i], inc, dec)


        decmax = max(dec, decmax)
        incmax = max(inc, incmax)
        # print(decmax)
        # print(incmax)
        
        return max(decmax, incmax)