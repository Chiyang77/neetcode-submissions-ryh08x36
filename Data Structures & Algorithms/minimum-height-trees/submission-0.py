class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = []
        minheight = float('inf')
        # print(adj)

        def bfs(q, level, visit):

            while q:
                q2 = []
                level+=1
                while q:
                    node = q.pop(0)
                    # print(node)
                    visit.add(node)
                    for nei in adj[node]:
                        if nei in visit:
                            continue
                        q2.append(nei)
                q = q2

            return level
                
        for i in range(n):
            q= []
            q.append(i)
            # print(i)
            level = bfs(q, 0, set())-1
            # print(level)
            # print('-'*10)
            if level < minheight:
                minheight = level
                res = []
                res.append(i)
            elif level == minheight:
                res.append(i)


        return res