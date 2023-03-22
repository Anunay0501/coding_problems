import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        ans = 0
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        
        while heap:
            smallestIndex, smallestIndex = heapq.heappop(heap)
            if marked[smallestIndex]:
                continue
            ans += smallestIndex
            marked[smallestIndex] = True

            if smallestIndex > 0:
                marked[smallestIndex - 1] = True

            if smallestIndex < n - 1:
                marked[smallestIndex + 1] = True
        return ans