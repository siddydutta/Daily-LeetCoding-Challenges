from itertools import product
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] != 1:
                continue
            perimeter += 4  # Add all four sides initially
            if i > 0:
                # check if left is island
                perimeter -= grid[i-1][j]
            if i < m-1:
                # check if right is island
                perimeter -= grid[i+1][j]
            if j > 0:
                # check if top is island
                perimeter -= grid[i][j-1]
            if j < n-1:
                # check if bottom is island
                perimeter -= grid[i][j+1]
        return perimeter


def main():
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    assert Solution().islandPerimeter(grid) == 16

    grid = [[1]]
    assert Solution().islandPerimeter(grid) == 4

    grid = [[1, 0]]
    assert Solution().islandPerimeter(grid) == 4


if __name__ == '__main__':
    main()
