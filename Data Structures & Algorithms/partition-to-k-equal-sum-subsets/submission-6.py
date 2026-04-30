class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0 :
            return False
        
        target = sum(nums)/k
        for n in nums:
            if n > target:
                return False

        nums.sort(reverse= True)

        def dfs(i,subsets):

            if i == len(nums):
                for sub in subsets:
                    if sub != target:
                        return False
                return True
            
            if i>len(nums):
                return False
            
            
            
            for j in range(len(subsets)):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                else:
                    continue

                if dfs(i+1, subsets):
                    return True
                subsets[j] -= nums[i]
                if subsets[j]==0:
                    break
            return False

        return dfs(0,[0]*k)