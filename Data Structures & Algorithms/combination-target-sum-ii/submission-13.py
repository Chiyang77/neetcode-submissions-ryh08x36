class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,currsum, subset):
            if i==len(candidates):
                if currsum == target and subset not in res:
                    res.append(subset)
                return 
            if currsum > target or i > len(candidates):
                return 
            dfs(i+1, currsum+candidates[i], subset+[candidates[i]])

            j=i
            while j<=len(candidates)-1 and candidates[j]== candidates[i]:

                j+=1

            dfs(j, currsum, subset)

        dfs(0,0,[])
        return res