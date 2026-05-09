class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if len(prerequisites)==0:
        #     return list(range(numCourses))

        adjlist = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjlist[course].append(pre)
        
        visit = set()
        q =[]

        def dfs(cour):
            print(cour)
            if not adjlist[cour] and cour not in q:
                q.append(cour)
                return True
            if cour in visit:
                return False

            pre = adjlist[cour]
            visit.add(cour)

            for p in pre:
                if not dfs(p):
                    return False
            adjlist[cour] = []
            visit.remove(cour)
            if cour not in q:
                q.append(cour)
            return True
         
            
        
        for n in range(numCourses):
            if n not in q:
                if not dfs(n):
                    return []
        return q