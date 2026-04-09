class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i,subset,total):
            if total==target:
                temp = subset.copy()
                res.append(temp)

                return 
            elif i >= len(candidates) or total>target:
                return

            num =candidates[i]
            subset.append(num)
            total += num
            dfs(i+1,subset, total)
            subset.pop()
            total -= num
            j=i
            while j+1 < len(candidates) and candidates[j+1] == candidates[j]:
                j+=1
            dfs(j+1,subset, total)

        
        dfs(0,[],0)
        return res