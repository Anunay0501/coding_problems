import collections
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frq = collections.Counter(nums)
        count = 0
        for key, val in frq.items():
            if val > count:
                count = val

        ans = [[] for _ in range(count)]
        for key, val in frq.items():
            for i in range(val):
                ans[i].append(key)

                
        return ans
