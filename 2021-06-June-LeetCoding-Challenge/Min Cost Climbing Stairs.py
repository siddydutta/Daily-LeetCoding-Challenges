# -*- coding: utf-8 -*-
from typing import List
from functools import lru_cache


class Solution1:
    '''
    Bottom up approach using recursion and memoization.
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def recursive(x):
            if x >= len(cost):
                return 0
            else:
                return cost[x] + min(recursive(x + 1), recursive(x + 2))

        return min(recursive(0), recursive(1))  # Start from bottom


class Solution2:
    '''
    Top down approach using recursion and memoization.
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]  # To reach top, simulate one last step

        @lru_cache(None)
        def recursive(x):
            if x == 0 or x == 1:
                return cost[x]
            else:
                return cost[x] + min(recursive(x - 1), recursive(x - 2))

        return recursive(len(cost) - 1)  # Start from top


class Solution3:
    '''
    Iterative bottom up approach, storing costs at each step.
    Space complexity: O(n).
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[i] for i in range(2)]
        dp += [0] * (n - 2)
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])


class Solution:
    '''
    Bottom up approach using constant space. Use only two previous steps.
    Space complexity: O(1), Time Complexity: O(n).
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = 0  # i-1 step
        dp2 = 0  # i-2 step
        for i in range(len(cost)):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)  # In-place swap
        return min(dp1, dp2)


if __name__ == '__main__':
    objects = [Solution(), Solution1(), Solution2(), Solution3()]
    for obj in objects:
        cost = [10, 15, 20]
        assert obj.minCostClimbingStairs(cost) == 15

        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        assert obj.minCostClimbingStairs(cost) == 6
