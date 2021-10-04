# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Straightforward solution.
    For every cell compute the perimeter by subtracting the number of
    adjacent island cells.
    Time Complexity: O(m*n)
    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4  # Add all four sides initially
                    if i > 0:
                        perimeter -= grid[i-1][j]  # Check if left is island
                    if i < m-1:
                        perimeter -= grid[i+1][j]  # Check if right is island
                    if j > 0:
                        perimeter -= grid[i][j-1]  # Check if top is island
                    if j < n-1:
                        perimeter -= grid[i][j+1]  # Check if bottom is island

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
