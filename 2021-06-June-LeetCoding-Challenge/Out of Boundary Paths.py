# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    '''
    Naive recursive solution, but uses a cache for memoization.
    '''
    def findPaths(self, m: int, n: int, maxMove: int,
                  startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            a = solve(i-1, j, maxMove-1)  # Left
            b = solve(i+1, j, maxMove-1)  # Right
            c = solve(i, j-1, maxMove-1)  # Top
            d = solve(i, j+1, maxMove-1)  # Bottom

            return a + b + c + d

        return solve(startRow, startColumn, maxMove) % (10**9 + 7)


def main():
    obj = Solution()
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    assert obj.findPaths(m, n, maxMove, startRow, startColumn) == 6

    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1
    assert obj.findPaths(m, n, maxMove, startRow, startColumn) == 12

    m = 8
    n = 50
    maxMove = 23
    startRow = 5
    startColumn = 26
    assert obj.findPaths(m, n, maxMove, startRow, startColumn) == 914783380


if __name__ == '__main__':
    main()
