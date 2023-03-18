from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        left, right = 1, (cars**2)*ranks[0]
        
        while left < right:
            m = (left+right)//2
            car = sum(int((m/right)**0.5) for right in ranks)
            if car >= cars:
                right = m
            else:
                left = m+1
        
        return left