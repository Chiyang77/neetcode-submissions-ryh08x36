
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_len = sum(matchsticks)
        
        if sum_len %4!=0:
            return False

        side_len = sum_len/4

        if max(matchsticks)> side_len:
            return False

        

        def dfs(i, sides):
            # print(i, sides)


            if i == len(matchsticks) and sides[0]==sides[1]== sides[2] == sides[3]:
                return True
            if sides[0] > side_len or sides[1]>side_len or sides[2]> side_len or sides[3]> side_len:
                return

            for j in range(4):
                sides[j]+=matchsticks[i]
                if dfs(i+1, sides):
                    return True
                else:
                    sides[j]-=matchsticks[i]
        res = dfs(0,[0]*4)
        if not res:
            return False
        return True