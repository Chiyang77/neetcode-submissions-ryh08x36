class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        half = sum(nums)/2
        def dfs(i, subsets):
            # print(i, subsets)
            if i == len(nums):
                return subsets[0]==subsets[1]

            for j in range(len(subsets)):

                if subsets[j]+nums[i]<= half:
                    subsets[j]+=nums[i]
                else:
                    continue

                if dfs(i+1, subsets):
                    return True
                subsets[j]-=nums[i]
            return False

        return dfs(0, [0]*2)
        