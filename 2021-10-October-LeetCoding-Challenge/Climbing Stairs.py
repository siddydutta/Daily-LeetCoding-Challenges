# -*- coding: utf-8 -*-
from functools import lru_cache


class RecursiveSolution:
    ''' Top down recursive solution with memoization. '''
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def climb(step: int) -> None:
            if step <= 2:
                return step  # Base case
            # Either go down one step or go down two steps
            return climb(step-1) + climb(step-2)
        return climb(n)


class DPSolution:
    ''' Bottom up dynamic programming solution. '''
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n  # Edge case
        # Only store previous two steps in DP array
        dp = [1, 2]  # Ways to reach 1st and 2nd step
        for step in range(3, n+1):
            # Next step can be reached using sum of ways to
            # reach previous two steps
            dp[0], dp[1] = dp[1], dp[0]+dp[1]
        return dp[-1]


def main():
    for obj in [RecursiveSolution(), DPSolution()]:
        n = 2
        assert obj.climbStairs(n) == 2

        n = 3
        assert obj.climbStairs(n) == 3

        n = 7
        assert obj.climbStairs(n) == 21

        n = 45
        assert obj.climbStairs(n) == 1836311903


if __name__ == '__main__':
    main()
