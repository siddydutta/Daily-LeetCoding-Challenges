# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            grid[x][y] = 1
            for dx, dy in d:
                if 0 <= x+dx <= m-1 and 0 <= y+dy <= n-1 \
                            and grid[x+dx][y+dy] == 0:
                    dfs(x+dx, y+dy)

        for i, j in product(range(m), range(n)):
            if grid[i][j] == 0 and (i == 0 or j == 0 or i == m-1 or j == n-1):
                dfs(i, j)

        count = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 0:
                dfs(i, j)
                count += 1
        return count


def main():
    grid = [[1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    assert Solution().closedIsland(grid) == 2

    grid = [[0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]]
    assert Solution().closedIsland(grid) == 1

    grid = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    assert Solution().closedIsland(grid) == 2


if __name__ == '__main__':
    main()
