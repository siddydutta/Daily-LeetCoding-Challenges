# -*- coding: utf-8 -*-
from functools import lru_cache
from itertools import product


class RecursiveSolution:
    ''' Recursive solution with memoization. '''
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(m, n):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1
            return dfs(m-1, n) + dfs(m, n-1)

        return dfs(m-1, n-1)


class DPSolution:
    ''' Bottom up tabulation solution. '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i, j in product(range(n), range(m)):
            if i == 0:
                dp[0][j] = 1  # First row is one move default
            if j == 0:
                dp[i][0] = 1  # First column is one move default
            if i != 0 and j != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Top and left sides

        return dp[-1][-1]


def main():
    for obj in [RecursiveSolution(), DPSolution()]:
        m, n = 3, 7
        assert obj.uniquePaths(m, n) == 28

        m, n = 3, 2
        assert obj.uniquePaths(m, n) == 3

        m, n = 7, 3
        assert obj.uniquePaths(m, n) == 28

        m, n = 3, 3
        assert obj.uniquePaths(m, n) == 6


if __name__ == '__main__':
    main()
