# -*- coding: utf-8 -*-
from functools import lru_cache
from math import inf
from typing import List


class Solution:
    ''' Recursive solution with memoization. '''
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @lru_cache(None)
        def move(i: int, j: int) -> int:
            if i >= m or j >= n:
                return inf

            if i == m-1 and j == n-1:
                # Reached princess, return health required
                if dungeon[i][j] > 0:
                    return 1  # Min health required is 1
                else:
                    return -dungeon[i][j] + 1  # Transform min health

            down_ans = move(i+1, j)  # Move downward
            right_ans = move(i, j+1)  # Move rightward
            # Return minimum health required, if possible else default 1
            return max(1, min(down_ans, right_ans) - dungeon[i][j])

        return move(0, 0)


def main():
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    assert Solution().calculateMinimumHP(dungeon) == 7

    dungeon = [[100]]
    assert Solution().calculateMinimumHP(dungeon) == 1


if __name__ == '__main__':
    main()
