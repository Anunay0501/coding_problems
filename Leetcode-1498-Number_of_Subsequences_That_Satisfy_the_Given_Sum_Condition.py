from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        res, mod = 0, 7 + 10**9
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r-l, mod)
                l += 1
        return res % mod
