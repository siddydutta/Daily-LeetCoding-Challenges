from itertools import product
from typing import List


class Solution:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            fish = grid[x][y]
            grid[x][y] = 0
            for dx, dy in self.DIRS:
                fish += dfs(x + dx, y + dy)
            return fish

        max_fish = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] != 0:
                max_fish = max(max_fish, dfs(i, j))
        return max_fish


def main():
    grid = [[0, 2, 1, 0],
            [4, 0, 0, 3],
            [1, 0, 0, 4],
            [0, 3, 2, 0]]
    assert Solution().findMaxFish(grid) == 7

    grid = [[1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]]
    assert Solution().findMaxFish(grid) == 1


if __name__ == '__main__':
    main()
