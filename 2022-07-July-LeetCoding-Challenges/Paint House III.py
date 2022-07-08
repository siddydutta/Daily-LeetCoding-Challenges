from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]],
                m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, j, k):
            if k > target:
                return inf

            if i == m:
                if k == target:
                    return 0
                else:
                    return inf

            if houses[i]:
                return dp(i+1, houses[i], k+(houses[i] != j))

            ans = inf
            for color, paint_cost in enumerate(cost[i], 1):
                ans = min(ans, paint_cost + dp(i+1, color, k+(color != j)))
            return ans

        res = dp(0, 0, 0)
        return res if res < inf else -1


def main():
    houses = [0, 0, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m, n, target = 5, 2, 3
    assert Solution().minCost(houses, cost, m, n, target) == 9


if __name__ == '__main__':
    main()
