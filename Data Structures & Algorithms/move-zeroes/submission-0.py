class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(len(nums)):
            if nums[i]!= 0:
                temp.append(nums[i])
            
        
        
        for i in range(len(nums)):
            if i <= len(temp)-1:
                nums[i]=temp[i]
            else:
                nums[i]=0