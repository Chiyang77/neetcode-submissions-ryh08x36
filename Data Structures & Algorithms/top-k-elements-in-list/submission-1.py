from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = sorted(cnt.items(), key=lambda x:x[1], reverse = True)
        ans = [a[0] for a in freq]
        return ans[:k]