# -*- coding: utf-8 -*-
from itertools import accumulate
from functools import lru_cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache
        def next_coin(i: int, rem: int) -> int:
            if i == len(piles) or rem == 0:
                return 0
            not_picked = next_coin(i+1, rem)
            picked = 0
            for j in range(min(len(piles[i]), rem)):
                picked = max(picked, piles[i][j]+next_coin(i+1, rem-j-1))
            return max(not_picked, picked)
        piles = list(map(list, map(accumulate, piles)))  # prefix sums
        return next_coin(0, k)


def main():
    piles = [[1, 100, 3],
             [7, 8, 9]]
    k = 2
    assert Solution().maxValueOfCoins(piles, k) == 101

    piles = [[100],
             [100],
             [100],
             [100],
             [100],
             [100],
             [1, 1, 1, 1, 1, 1, 700]]
    k = 7
    assert Solution().maxValueOfCoins(piles, k) == 706


if __name__ == '__main__':
    main()
