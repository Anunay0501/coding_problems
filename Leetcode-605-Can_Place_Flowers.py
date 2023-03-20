from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ind, count = 0, 0
        while ind < len(flowerbed):
            if flowerbed[ind] == 0:
                if (ind-1 > -1 and flowerbed[ind-1]) != 0 or (ind+1 < len(flowerbed) and flowerbed[ind+1]) != 0:
                    ind += 1
                else:
                    count += 1
                    ind += 2
            else:
                ind += 1
        return count >= n
