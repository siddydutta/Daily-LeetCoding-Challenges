# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    '''
    BFS Solution.
    Time Complexity: O(m*n)
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])  # Rows, Columns

        queue = list()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    # If cell is zero, then distance to nearest zero is zero
                    queue.append((row, col))  # For BFS
                else:
                    mat[row][col] = None

        # Adjacent cells -> Right, Left, Bottom, Top
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                for adj_row, adj_col in directions:
                    next_row, next_col = row + adj_row, col + adj_col
                    # Check if next cell is within bounds and needs to find
                    # a nearest zero cell
                    if (next_row < 0 or next_row >= m) or \
                        (next_col < 0 or next_col >= n) or \
                            mat[next_row][next_col] is not None:
                        continue
                    # Next cell is zero
                    mat[next_row][next_col] = dist
                    queue.append((next_row, next_col))
            dist += 1

        return mat


class Solution:
    ''' One pass solution. '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])  # Rows, Columns
        found, level = True, 0

        while found:
            found = False
            level += 1
            for row in range(m):
                for col in range(n):
                    if mat[row][col] == level:
                        if not (row < m-1 and mat[row+1][col] < level or
                                row > 0 and mat[row-1][col] < level or
                                col < n-1 and mat[row][col+1] < level or
                                col > 0 and mat[row][col-1] < level):
                            mat[row][col] += 1
                            found = True

        return mat


def main():
    mat = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    ans = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    assert Solution().updateMatrix(mat) == ans

    mat = [[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]
    ans = [[0, 0, 0],
           [0, 1, 0],
           [1, 2, 1]]
    assert Solution().updateMatrix(mat) == ans


if __name__ == '__main__':
    main()
