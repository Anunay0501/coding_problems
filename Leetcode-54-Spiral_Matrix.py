from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        l, r, t, b = 0, n, 0, m
        i, j, di, dj = 0, 0, 0, 1
        for _ in range(m*n):
            ans.append(matrix[i][j])

            if not t <= i + di < b or not l <= j + dj < r:
                if dj == 1:
                    t += 1
                elif di == 1:
                    r -= 1
                elif dj == -1:
                    b -= 1
                else:
                    l += 1

                di, dj = dj, -di

            i += di
            j += dj
        return ans
