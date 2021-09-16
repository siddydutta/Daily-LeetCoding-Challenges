# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Straightforward solution.
    Time Complexity: (mn)
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])  # Total rows, total cols
        k, l = 0, 0  # Starting row, col index
        result = list()

        while k < m and l < n:
            # Access cols of top row
            for col in range(l, n):
                result.append(matrix[k][col])
            k += 1  # Reduce top row
            # Access rows of last col
            for row in range(k, m):
                result.append(matrix[row][n-1])
            n -= 1  # Reduce last col

            # Access cols of last row, if possible
            if k < m:
                for col in range(n-1, l-1, -1):
                    result.append(matrix[m-1][col])
                m -= 1  # Reduce last row
            # Access rows of first col, if possible
            if l < n:
                for row in range(m-1, k-1, -1):
                    result.append(matrix[row][l])
                l += 1  # Reduce first col

        return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert Solution().spiralOrder(matrix) == expected


if __name__ == '__main__':
    main()
