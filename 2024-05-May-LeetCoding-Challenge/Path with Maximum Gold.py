from itertools import product
from typing import List


class Solution:
    DELTA = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def mine(x: int, y: int) -> int:
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return 0
            curr_max = 0
            gold = grid[x][y]
            grid[x][y] = 0
            for dx, dy in self.DELTA:
                curr_max = max(curr_max, mine(x+dx, y+dy))
            grid[x][y] = gold
            return curr_max + gold

        ans = 0
        for row, col in product(range(rows), range(cols)):
            ans = max(ans, mine(row, col))
        return ans


def main():
    grid = [[0, 6, 0],
            [5, 8, 7],
            [0, 9, 0]]
    assert Solution().getMaximumGold(grid) == 24

    grid = [[1, 0, 7],
            [2, 0, 6],
            [3, 4, 5],
            [0, 3, 0],
            [9, 0, 20]]
    assert Solution().getMaximumGold(grid) == 28


if __name__ == '__main__':
    main()
