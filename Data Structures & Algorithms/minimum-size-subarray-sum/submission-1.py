class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0, 0 
        curr = nums[l]
        minlen = float('inf')

        while l<=r and r <len(nums):

            if r !=0:
                curr+=nums[r]

            # print(curr)
            if curr< target:
                r+=1

            else:

                # print(l,r)
                # print('-'*10)
                minlen = min(minlen, r-l+1)
                curr -= nums[l]
                curr -= nums[r]
                l+=1
                
        return minlen if minlen!=float('inf') else 0