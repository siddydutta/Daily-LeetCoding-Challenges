# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Solution that involves storing the positions of zero.
    Time Complexity: O(mn)
    Space Complexity: O(m+n)
    '''
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()  # Set of row indices containing a zero
        zero_cols = set()  # Set of col indices containing a zero

        # Store positions of zero
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Set zero if row or col is recorded to have a zero
        for row in range(rows):
            for col in range(cols):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0

        return matrix


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert Solution().setZeroes(matrix) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    assert Solution().setZeroes(matrix) == [[0, 0, 0, 0],
                                            [0, 4, 5, 0],
                                            [0, 3, 1, 0]]

    matrix = [[1, 2, 3, 4],
              [5, 0, 7, 8],
              [0, 10, 11, 12],
              [13, 14, 15, 0]]
    assert Solution().setZeroes(matrix) == [[0, 0, 3, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0]]


if __name__ == '__main__':
    main()
