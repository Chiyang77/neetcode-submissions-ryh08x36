class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # visit = set()
        # directions = [[1,0], [0,1]]
        cache = {}
        def dfs(r,c):
            # print(r,c)
            if r>=m or c>=n:
                return 0
            if r==m-1 and c == n-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]


            cache[(r,c)] = dfs(r+1,c)+dfs(r,c+1)

            return cache[(r,c)]

        return dfs(0,0)