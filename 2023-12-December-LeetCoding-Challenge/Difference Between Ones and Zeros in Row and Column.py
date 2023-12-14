from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row1s, col1s = defaultdict(int), defaultdict(int)
        for i, j in product(range(m), range(n)):
            row1s[i] += grid[i][j]
            col1s[j] += grid[i][j]
        for i, j in product(range(m), range(n)):
            # grid[i][j] = row1s[i] + col1s[j] - (n-row1s[i]) - (m-col1s[j])
            grid[i][j] = 2*row1s[i] + 2*col1s[j] - n - m
        return grid


def main():
    grid = [[0, 1, 1],
            [1, 0, 1],
            [0, 0, 1]]
    assert Solution().onesMinusZeros(grid) == [[0, 0, 4],
                                               [0, 0, 4],
                                               [-2, -2, 2]]

    grid = [[1, 1, 1],
            [1, 1, 1]]
    assert Solution().onesMinusZeros(grid) == [[5, 5, 5],
                                               [5, 5, 5]]


if __name__ == '__main__':
    main()
