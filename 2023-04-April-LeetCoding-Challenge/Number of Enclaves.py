# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            grid[x][y] = 0
            for dx, dy in d:
                if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy]:
                    dfs(x+dx, y+dy)

        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1 and (i == 0 or j == 0 or i == m-1 or j == n-1):
                dfs(i, j)
        return sum(sum(row) for row in grid)


def main():
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert Solution().numEnclaves(grid) == 3

    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    assert Solution().numEnclaves(grid) == 0


if __name__ == '__main__':
    main()
