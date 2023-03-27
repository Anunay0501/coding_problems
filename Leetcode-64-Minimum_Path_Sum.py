# First attempt to deal with a dp problem. Tried understanding  how to do break down the problem.
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # minSBR=grid[-1]]-1+min(sum(grid[-1][-2]),sum(grid[-2][-1]))
        m, n = len(grid), len(grid[0])
        dp = [[None for _ in range(n)] for a in range(m)]
        dp[0][0] = grid[0][0]

        def cal(i, j):

            if i-1 > -1 and dp[i-1][j] == None:
                cal(i-1, j)
            if j-1 > -1 and dp[i][j-1] == None:
                cal(i, j-1)
            summ = 0
            if i-1 > -1 and j-1 > -1:
                summ = min(dp[i-1][j], dp[i][j-1])
            elif i-1 > -1:
                summ = dp[i-1][j]
            elif j-1 > -1:
                summ = dp[i][j-1]
            dp[i][j] = grid[i][j]+summ
        cal(m-1, n-1)
        return dp[m-1][n-1]

# Second attempt. After reviewing other solutions made some changes. Change in original grid should not be done but it's just for a clearer solution.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
