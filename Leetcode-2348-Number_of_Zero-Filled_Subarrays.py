from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = left = 0
        for right, dig in enumerate(nums):
            if dig != 0:
                left = right
            else:
                if nums[left] != 0:
                    left = right
                ans += (right-left+1)
        return ans
