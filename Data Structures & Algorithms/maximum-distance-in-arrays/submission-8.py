class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        ans = 0

        for i in range(1,len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            ans = max(ans,max(global_max-curr_min, curr_max-global_min))
            global_min = min(global_min, curr_min)
            global_max = max(global_max, curr_max)
        
        return ans