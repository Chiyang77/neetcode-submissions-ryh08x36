class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for n in nums:
            sum+=n
            self.prefix.append(sum)
               

    def sumRange(self, left: int, right: int) -> int:
        
        preright = self.prefix[right]
        preleft = self.prefix[left-1] if left >0 else 0

        return preright-preleft

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)