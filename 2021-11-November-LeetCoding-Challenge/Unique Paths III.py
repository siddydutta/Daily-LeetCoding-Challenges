# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Solution:
    ''' Backtracking based solution. '''
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        def dfs(x, y, rem):
            if x < 0 or x >= m or y < 0 or y >= n:
                return  # Out of grid
            if grid[x][y] is None or grid[x][y] == -1:
                return  # Cell visited or obstacle present
            if grid[x][y] == 2 and rem == 0:
                nonlocal ans
                ans += 1  # Reached ending square

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                temp = grid[x][y]  # Temp variable to maintain state
                grid[x][y] = None  # Mark as visited
                dfs(x+dx, y+dy, rem-1)
                grid[x][y] = temp  # For backtracking

        empty = 0
        # Find starting cell and number of empty cells
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 1:
                sx, sy = x, y
                continue
            if grid[x][y] != -1:
                empty += 1

        dfs(sx, sy, empty)
        return ans


def main():
    grid = [[1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]]
    assert Solution().uniquePathsIII(grid) == 2

    grid = [[1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]]
    assert Solution().uniquePathsIII(grid) == 4

    grid = [[0, 1],
            [2, 0]]
    assert Solution().uniquePathsIII(grid) == 0


if __name__ == '__main__':
    main()
