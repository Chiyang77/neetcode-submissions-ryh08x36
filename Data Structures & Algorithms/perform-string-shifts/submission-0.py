class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for dir,n in shift:
            if dir == 0:
                while n>0:
                    s = s[1:]+s[0]
                    n-=1
            elif dir ==1:
                while n>0:
                    s = s[-1]+s[:-1]
                    n-=1
        return s