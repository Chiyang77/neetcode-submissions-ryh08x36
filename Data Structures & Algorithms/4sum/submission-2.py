class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for a in range(0,n):
            for b in range(a+1,n):
                c = b+1
                d = n-1
                while d>c:
                    total = nums[a]+nums[b]+nums[c]+nums[d]
                    # print(a,b,c,d)
                    if total==target:
                        res.add((nums[a],nums[b], nums[c], nums[d]))
                        c+=1
                        d-=1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1
        return list(res)