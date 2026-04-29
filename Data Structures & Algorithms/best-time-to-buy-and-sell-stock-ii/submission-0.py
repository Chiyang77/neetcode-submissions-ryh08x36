class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0

        res = 0
        prev = prices[0]
        for n in prices[1:]:
            if n>=prev:
                res += (n-prev)
            
            prev = n
        return res