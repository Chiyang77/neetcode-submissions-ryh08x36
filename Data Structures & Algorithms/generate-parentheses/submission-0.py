class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(remain, unclose, curr):
            if remain <0:
                return
            # print(remain, unclose, curr)
            if remain == 0 and unclose >0:

                while unclose > 0:
                    curr += ")"
                    unclose -=1
                res.append(curr)
                return

            if remain!= 0:
                if unclose == 0:
                    dfs(remain-1, unclose+1, curr+"(")
                else:
                    dfs(remain, unclose-1, curr+")")
                    dfs(remain-1, unclose+1, curr+"(")


        dfs(n, 0, "")
        # print(res)
        return res