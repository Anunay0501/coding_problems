import heapq
from typing import List

# Original solution I came up with. If mouse2 ate all cheeses then we have to choose k cheeses for mouse1 we chose those where reward1[i]-reward2[i] is highest. hence the heap.

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n=len(reward1)
        ans=sum(reward2)
        heap=[]
        if k==0:
            return ans
        for i in range(n):
            profit=reward1[i]-reward2[i]
            if len(heap)<k:
                heapq.heappush(heap,profit)
            else:
                if heap[0]< profit:
                    heapq.heapreplace(heap,profit)

        return ans+sum(heap)

#One line solution. Courtesy- @lee215
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        return sum(reward2) + sum(heapq.nlargest(k, (a - b for a, b in zip(reward1, reward2))))