class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        nums = range(num)
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if m**2>num:
                r=m-1
            elif m**2<num:
                l = m+1
            else:
                return True
        
        return False