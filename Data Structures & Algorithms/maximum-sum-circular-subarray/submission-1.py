class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        newnums = nums+nums
        maxsum = float('-inf')

        for i in range(len(newnums)):
            curr = newnums[i]
            for j in range(i, len(newnums)):
                if j-i <= len(nums)-1 and i!=j:
                    curr+=newnums[j]
                maxsum = max(curr,maxsum)
                # print(i,j, maxsum)
        # print(newnums,)
        return maxsum