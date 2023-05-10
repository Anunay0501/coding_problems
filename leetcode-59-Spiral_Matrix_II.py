from typing import List


# inspired from Spiral Matrix I
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for i in range(n)]
        l, r, t, b = 0, n, 0, n
        i, j, di, dj = 0, 0, 0, 1
        for num in range(1, (n*n)+1):
            ans[i][j] = num

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


# ingenious use of non zero elements, found in discussions
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x = [[0]*n for row in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            x[i][j] = k+1
            if x[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return x
