class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(curr,prev,visit):
            if curr in visit:
                return True

            visit.add(curr)

            for nei in adj[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr, visit):
                    return True
            return False

        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()
            if dfs(u, -1,  visit):
                return [u,v]
