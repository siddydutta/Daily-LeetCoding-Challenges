# -*- coding: utf-8 -*-
from functools import lru_cache
from itertools import product
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ''' DFS based solution using memoization. '''
        m, n = len(grid), len(grid[0])
        moves = [(1, -1), (1, 0), (1, 1)]  # Possible next moves from a cell

        @lru_cache(None)
        def dfs(i: int, j: int, x: int, y: int) -> int:
            ''' (i, j) and (x, y) are the positions of the robots. '''
            if i == x == m or j < 0 or j >= n or y < 0 or y >= n:
                return 0   # Out of bounds base condition

            res = 0
            for (di, dj), (dx, dy) in product(moves, moves):
                # Add both cells only if robots are in different cells
                val = grid[i][j] if i == x and j == y else grid[i][j]+grid[x][y]
                # Update max using DFS through possible moves
                res = max(res, val+dfs(i+di, j+dj, x+dx, y+dy))
            return res

        return dfs(0, 0, 0, n-1)  # Initial robot positions


def main():
    grid = [[3, 1, 1],
            [2, 5, 1],
            [1, 5, 5],
            [2, 1, 1]]
    assert Solution().cherryPickup(grid) == 24

    grid = [[1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6]]
    assert Solution().cherryPickup(grid) == 28


if __name__ == '__main__':
    main()
