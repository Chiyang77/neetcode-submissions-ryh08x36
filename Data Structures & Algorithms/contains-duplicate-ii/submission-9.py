from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash = set()
        L = 0
        for R in range(0,len(nums)):
            # print(L,R)
            if R-L > k:
                hash.remove(nums[L])
                L+=1
            if nums[R] not in hash:
                hash.add(nums[R])
            else:
                return True
            # print(hash)

        return False