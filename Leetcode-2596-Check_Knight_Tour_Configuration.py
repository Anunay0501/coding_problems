from collections import deque
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        queue = deque([(0, 0)])
        ans = 0

        while queue:
            ans += 1
            x, y = queue.popleft()

            for row, col in [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2), (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)]:
                if 0 <= row < n and 0 <= col < n and grid[row][col] == grid[x][y] + 1:
                    queue.append((row, col))

        return ans == pow(n, 2)
