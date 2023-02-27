# -*- coding: utf-8 -*-
from itertools import product
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def __is_leaf(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        return all(grid[i][j] == grid[0][0]
                   for i, j in product(range(rows), range(cols)))

    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        if self.__is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        rows, cols = len(grid), len(grid[0])
        rows_div, cols_div = rows // 2, cols // 2
        return Node(
            None,
            False,
            self.construct([row[:cols_div] for row in grid[:rows_div]]),
            self.construct([row[cols_div:] for row in grid[:rows_div]]),
            self.construct([row[:cols_div] for row in grid[rows_div:]]),
            self.construct([row[cols_div:] for row in grid[rows_div:]]))


def main():
    grid = Solution().construct([[0, 1],
                                 [1, 0]])
    assert not grid.val
    assert not grid.isLeaf
    assert grid.topLeft.val == 0
    assert grid.topLeft.isLeaf
    assert grid.topRight.val == 1
    assert grid.topRight.isLeaf
    assert grid.bottomLeft.val == 1
    assert grid.bottomLeft.isLeaf
    assert grid.bottomRight.val == 0
    assert grid.bottomRight.isLeaf

    grid = Solution().construct([[1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0]])
    assert not grid.val
    assert not grid.isLeaf
    assert grid.topLeft.val == 1
    assert grid.topLeft.isLeaf
    assert not grid.topRight.val
    assert not grid.topRight.isLeaf
    assert grid.topRight.topLeft.val == 0
    assert grid.topRight.topLeft.isLeaf
    assert grid.topRight.topRight.val == 0
    assert grid.topRight.topRight.isLeaf
    assert grid.topRight.bottomLeft.val == 1
    assert grid.topRight.bottomLeft.isLeaf
    assert grid.topRight.bottomRight.val == 1
    assert grid.topRight.bottomRight.isLeaf
    assert grid.bottomLeft.val == 1
    assert grid.bottomLeft.isLeaf
    assert grid.bottomRight.val == 0
    assert grid.bottomRight.isLeaf


if __name__ == '__main__':
    main()
