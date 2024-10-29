from functools import lru_cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(x: int, y: int) -> int:
            max_moves = 0
            for dx, dy in ((-1, 1), (0, 1), (1, 1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    max_moves = max(max_moves, 1+dfs(nx, ny))
            return max_moves

        return max(dfs(i, 0) for i in range(m))


def main():
    grid = [[2, 4, 3, 5],
            [5, 4, 9, 3],
            [3, 4, 2, 11],
            [10, 9, 13, 15]]
    assert Solution().maxMoves(grid) == 3

    grid = [[3, 2, 4],
            [2, 1, 9],
            [1, 1, 7]]
    assert Solution().maxMoves(grid) == 0


if __name__ == '__main__':
    main()
