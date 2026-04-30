class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_1st = trust[0][1]
        for i in range(1,n):
            if trust[i-1][1]!= trust_1st:
                return -1

        # print(trust)
        for i in range(len(trust)):
            if trust[i][0]==trust_1st:
                return -1

        return trust_1st