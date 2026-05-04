from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = [[nums[0]]]
        nums.pop(0)
        while nums:
            n = nums.pop(0)
            # print(n)
            for _ in range(len(res)):
                # print(res)
                r = res.pop(0)
                # print(r)
                for i in range(len(r)+1):
                    r.insert(i,n) 
                    # print(r)
                    if r not in res:
                        res.append(r.copy())
                    # print(res)
                    # print('-'*10)
                    r.pop(i)

        return res