from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        for cour, pre in prerequisites:
            adjlist[cour].append(pre)

        visit = set()
        
        def dfs(cour):
            if not adjlist[cour]:
                return True
            if cour in visit:
                return False
            
            visit.add(cour)
            for pre in adjlist[cour]:
                if not dfs(pre):
                    return False
            adjlist[cour]= []
            visit.remove(cour)
            return True
            

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True