from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans, curr = 0, 0
        
        for num in nums:                                # We can alternately use accumulate.
            ans += 1
            curr += num
            if curr <= 0:
                return ans-1
        
        return ans