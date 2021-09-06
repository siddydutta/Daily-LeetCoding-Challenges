# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import List


class Solution:
    ''' Game theory solution. Since Alex always starts first, Alex wins. '''
    def stoneGame(self, piles: List[int]) -> bool:
        return True


class Solution1:
    ''' Recursive solution with memoization. '''
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def pick_stone(start: int, end: int):
            if (start > end):
                return 0
            return max(piles[start] - pick_stone(start+1, end),
                       piles[end] - pick_stone(start, end-1))

        return pick_stone(0, len(piles)-1) > 0


class Solution2:
    ''' Dynamic programming solution. '''
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for start in range(n-1):
            for end in range(n-1, 0, -1):
                if start > end:
                    continue
                dp[start][end] = max(piles[start] - dp[start+1][end],
                                     piles[end] - dp[start][end-1])
        return dp[0][n-1] > 0


def main():
    solutions = [Solution(), Solution1(), Solution2()]

    for obj in solutions:
        piles = [5, 3, 4, 5]
        assert obj.stoneGame(piles)

        piles = [7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12,
                 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11, 50, 16, 50,
                 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42,
                 46, 24]
        assert obj.stoneGame(piles)


if __name__ == '__main__':
    main()
