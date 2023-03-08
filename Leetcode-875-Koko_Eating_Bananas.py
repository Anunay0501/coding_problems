from math import ceil


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        lo, hi = 1, 10**9                     
        
        while lo < hi:
            m = lo+(hi-lo)//2
            req = sum(ceil(banana/m) for banana in piles)
        
            if req <= h:
                hi = m
            else:
                lo = m+1
        
        return lo

# Time complexity - nlogk