import heapq


class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        ans = sum(gifts)
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            x = -gifts[0]
            heapq.heapreplace(gifts, -int(x**0.5))
            ans -= (x-int(x**0.5))

        return ans