# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def __dfs(self, grid, row, col):
        # Check if row is out of bounds
        if row < 0 or row >= len(grid):
            return 0
        # Check if col is out of bounds
        if col < 0 or col >= len(grid[row]):
            return 0
        # Check if cell is non-island
        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0  # Reset cell to prevent repeated counting
        count = 1
        # Recursive DFS
        count += self.__dfs(grid, row-1, col)  # Top
        count += self.__dfs(grid, row+1, col)  # Bottom
        count += self.__dfs(grid, row, col+1)  # Right
        count += self.__dfs(grid, row, col-1)  # Left
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # If cell is island, check max area using DFS
                if grid[row][col] == 1:
                    max_area = max(max_area, self.__dfs(grid, row, col))
        return max_area


if __name__ == '__main__':
    obj = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    max_area = obj.maxAreaOfIsland(grid)
    assert max_area == 6
