from typing import List

# area = (distance between two heights) x (min(height1, height2)). To maximize 1st part - start from extreme left and right.
# we can move pointer with lesser height towards other And keep updating the maximum area recorded and return it.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        ans = 0

        while l < r:
            area = (r-l) * (min(height[l], height[r]))
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans