# -*- coding: utf-8 -*-
from itertools import product
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([(i, j, i, j)
                       for i, j in product(range(rows), range(cols))
                       if grid[i][j] == 1])
        visited, res = set(), -1

        while queue:
            row, col, x, y = queue.popleft()
            if not 0 <= row < rows or not 0 <= col < cols:
                continue
            if (row, col) not in visited:
                visited.add((row, col))
                if (row, col) != (x, y):
                    res = max(res, abs(row-x)+abs(col-y))
                for dx, dy in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                    nx, ny = row+dx, col+dy
                    queue.append((nx, ny, x, y))
        return res


def main():
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert Solution().maxDistance(grid) == 2

    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert Solution().maxDistance(grid) == 4


if __name__ == '__main__':
    main()
