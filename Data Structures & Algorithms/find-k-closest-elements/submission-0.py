class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(n-x) for n in arr]
        sort_diff_arr = [val for dif, val in sorted(zip(diff, arr))]
        res = sort_diff_arr[:k]
        res.sort()

        return res
        