# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List


class NaiveSolution:
    '''
    Brute force solution.
    Toggle every zero in the grid and check the area of the island.
    Time Complexity: O(n^4) -> Leads to TLE.
    '''
    def getArea(self, grid: List[List[int]], row: int, col: int) -> int:
        ''' Returns area of the island using DFS. '''
        # Base condition -> Check if row and column are within bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
            return 0
        # Base condition -> Grid cell is not an island
        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0  # To prevent counting cell again
        area = 1
        area += self.getArea(grid, row-1, col)  # Top
        area += self.getArea(grid, row+1, col)  # Bottom
        area += self.getArea(grid, row, col-1)  # Left
        area += self.getArea(grid, row, col+1)  # Right
        return area

    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)  # Grid is NxN
        is_zero_present = False  # Flag to check if any zero present in grid

        max_area = 0
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 0:
                    is_zero_present = True
                    grid[row][col] = 1  # Toggle to 1
                    # A copy of the grid is passed to retain original grid
                    max_area = max(max_area,
                                   self.getArea(deepcopy(grid), row, col))
                    grid[row][col] = 0  # Toggle back to 0

        if not is_zero_present:
            max_area = N*N  # No zeros present, max area is full grid
        return max_area


class Solution:
    '''
    Builds on the brute force approach.
    Tag and map a connected component to its total area.
    For every zero in the grid, a possible area is the sum of the areas of its
    neigbouring connected components.
    Time Complexity: O(n^2)
    '''
    def __init__(self):
        self.islands = dict()  # IslandID -> IslandArea
        self.islands[0] = 0  # Default
        self.islandId = 2

    def tagIsland(self, grid: List[List[int]], row: int, col: int) -> int:
        ''' Tags connected components and returns total area of island. '''
        # Base condition -> Check if row and column are within bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
            return 0
        # Base condition -> Grid cell is not an island
        if grid[row][col] != 1:
            return 0

        grid[row][col] = self.islandId  # Tag cell with island ID
        area = 1
        area += self.tagIsland(grid, row-1, col)  # Top
        area += self.tagIsland(grid, row+1, col)  # Bottom
        area += self.tagIsland(grid, row, col-1)  # Left
        area += self.tagIsland(grid, row, col+1)  # Right
        return area

    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)  # Grid is NxN

        # First iteration tags every connected component (island)
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 1:
                    area = self.tagIsland(grid, row, col)
                    self.islands[self.islandId] = area
                    self.islandId += 1

        # Second iteration checks every non-island cell and computes area
        # using neighbouring islands
        max_area = 0
        is_zero_present = False  # Flag to check if any zero present in grid
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 0:
                    is_zero_present = True
                    n_Areas = set()  # For distinct neighbour island IDs
                    n_Areas.add(grid[row-1][col] if row > 0 else 0)  # Top
                    n_Areas.add(grid[row+1][col] if row < N-1 else 0)  # Bottom
                    n_Areas.add(grid[row][col-1] if col > 0 else 0)  # Left
                    n_Areas.add(grid[row][col+1] if col < N-1 else 0)  # Right
                    total_area = 1  # Count current grid as island
                    for islandId in n_Areas:
                        total_area += self.islands.get(islandId)
                    max_area = max(max_area, total_area)

        if not is_zero_present:
            max_area = N*N  # No zeros present, max area is full grid
        return max_area


def main():
    grid = [[1, 0],
            [0, 1]]
    assert Solution().largestIsland(grid) == 3

    grid = [[1, 1],
            [1, 0]]
    assert Solution().largestIsland(grid) == 4

    grid = [[1, 1],
            [1, 1]]
    assert Solution().largestIsland(grid) == 4

    grid = [[0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 1, 0]]
    assert Solution().largestIsland(grid) == 7

    grid = [[0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 0]]
    assert Solution().largestIsland(grid) == 18


if __name__ == '__main__':
    main()
