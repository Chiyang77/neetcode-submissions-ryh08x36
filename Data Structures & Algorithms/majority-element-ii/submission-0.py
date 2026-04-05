from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res =[]
        size = len(nums)//3
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1
        res =[key for key, val in hashmap.items() if val> size]
        return res