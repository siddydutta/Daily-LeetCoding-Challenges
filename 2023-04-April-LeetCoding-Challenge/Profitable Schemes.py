# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, curr: int, people: int) -> int:
            if i >= len(group):
                return curr >= minProfit
            ways = 0
            if people + group[i] <= n:
                ways += dfs(i+1, min(minProfit, curr+profit[i]), people+group[i])
            ways += dfs(i+1, curr, people)
            return ways
        return dfs(0, 0, 0) % int(1e9+7)


def main():
    n, minProfit, group, profit = 5, 3, [2, 2], [2, 3]
    assert Solution().profitableSchemes(n, minProfit, group, profit) == 2

    n, minProfit, group, profit = 10, 5, [2, 3, 5], [6, 7, 8]
    assert Solution().profitableSchemes(n, minProfit, group, profit) == 7


if __name__ == '__main__':
    main()
