from itertools import product
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x: int, y: int) -> None:
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != '1':
                return
            grid[x][y] = None
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(x+dx, y+dy)

        count = 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == '1':
                dfs(row, col)
                count += 1
        return count


def main():
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    assert Solution().numIslands(grid) == 1

    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    assert Solution().numIslands(grid) == 3


if __name__ == '__main__':
    main()
