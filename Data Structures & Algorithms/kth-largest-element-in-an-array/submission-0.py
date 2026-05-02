class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-n for n in nums]
        heapq.heapify(maxheap)
        res = []
        for _ in range(k-1):
            heapq.heappop(maxheap)
        return -heapq.heappop(maxheap)