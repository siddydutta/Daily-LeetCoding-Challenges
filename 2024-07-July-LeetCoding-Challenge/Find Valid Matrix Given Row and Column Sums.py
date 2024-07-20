from itertools import product
from typing import List


class Solution:
    def restoreMatrix(
            self, row_sum: List[int], col_sum: List[int]
    ) -> List[List[int]]:
        m, n = len(row_sum), len(col_sum)
        matrix = [[None]*n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            matrix[i][j] = min(row_sum[i], col_sum[j])
            row_sum[i] -= matrix[i][j]
            col_sum[j] -= matrix[i][j]
        return matrix


def main():
    row_sum = [3, 8]
    col_sum = [4, 7]
    assert Solution().restoreMatrix(row_sum, col_sum) == [[3, 0],
                                                          [1, 7]]

    row_sum = [5, 7, 10]
    col_sum = [8, 6, 8]
    assert Solution().restoreMatrix(row_sum, col_sum) == [[5, 0, 0],
                                                          [3, 4, 0],
                                                          [0, 2, 8]]


if __name__ == '__main__':
    main()
