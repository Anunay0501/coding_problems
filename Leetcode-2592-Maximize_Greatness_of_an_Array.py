import collections
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        frq = collections.Counter(nums)
        ans = 0
        bigger = 0
        for key in sorted(frq, reverse=True):
            if bigger:
                if bigger >= frq[key]:
                    ans += frq[key]
                else:
                    ans += bigger
                    bigger = frq[key]
            else:
                bigger = frq[key]
        return ans
