from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        q = []
        q.append(("0000",0))

        visit = set(deadends)

        def children(curr):
            res = []
            for i in range(len(curr)):
                res.append(curr[:i]+str((int(curr[i])+1)%10)+curr[i+1:])
                res.append(curr[:i]+str((int(curr[i])-1+10)%10)+curr[i+1:])
            return res


        while q:
            curr,cnt = q.pop(0)
            if curr ==target:
                return cnt
            childrens = children(curr)
            for child in childrens:
                if child not in visit:
                    visit.add(child)
                    q.append((child,cnt+1))             

        return -1       
