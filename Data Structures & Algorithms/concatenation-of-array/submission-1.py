class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = []
        n = len(nums)
        new_array = nums+nums
        return new_array