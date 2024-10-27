from functools import lru_cache
from itertools import product
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def recursive(i: int, j: int) -> int:
            if i == m or j == n or matrix[i][j] == 0:
                return 0
            return 1 + min(recursive(i+1, j),
                           recursive(i, j+1),
                           recursive(i+1, j+1))

        n_squares = 0
        for i, j in product(range(m), range(n)):
            n_squares += recursive(i, j)
        return n_squares


def main():
    matrix = [[0, 1, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1]]
    assert Solution().countSquares(matrix) == 15

    matrix = [[1, 0, 1],
              [1, 1, 0],
              [1, 1, 0]]
    assert Solution().countSquares(matrix) == 7


if __name__ == '__main__':
    main()
