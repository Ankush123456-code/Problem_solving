from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache
        def dfs(i, j):
            nonlocal grid
            if (i >= len(grid)) or (j >= len(grid[0])):
                return 1e9
            if (i == len(grid) - 1) and (j == len(grid[0]) - 1):
                return grid[i][j]
            left = dfs(i + 1, j)
            right = dfs(i, j + 1)

            ans = min(left, right) + grid[i][j]
            return ans

        return dfs(0, 0)
