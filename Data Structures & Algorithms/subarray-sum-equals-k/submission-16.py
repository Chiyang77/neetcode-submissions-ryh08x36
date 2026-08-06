from typing import List
import numpy as np
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = np.cumsum(nums)
        seen={0:1}
        currsum = 0
        cnt = 0
        for i in range(len(nums)):
            currsum += nums[i]
            cnt += seen.get(currsum-k,0)
            seen[currsum] = seen.get(currsum,0)+1
        return cnt