class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        n = range(1, x+1)
        l, r= 1, x
        prev = 0
        while l<r:
            
            m = (l+r)//2
            if prev ==m:
                return m
            if m*m > x:
                r = m                

            elif m*m < x:
                l = m
            else:
                return m
            prev = m
        return m
