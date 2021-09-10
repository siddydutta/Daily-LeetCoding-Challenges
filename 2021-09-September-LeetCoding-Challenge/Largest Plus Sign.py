# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    '''
    Dynamic programming based solution.
    Time Complexity: O(n^2)
    '''
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Create grid with mines
        grid = [[1 for _ in range(n)] for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0

        dp = [[inf for _ in range(n)] for _ in range(n)]  # Maintains k
        # Left to Right Traversal of Grid
        for x in range(n):
            s = 0
            for y in range(n):
                if grid[x][y] == 0:
                    s = 0
                else:
                    s += 1
                dp[x][y] = min(dp[x][y], s)  # k should be minimum
        # Right to Left Traversal of Grid
        for x in range(n):
            s = 0
            for y in range(n-1, -1, -1):
                if grid[x][y] == 0:
                    s = 0
                else:
                    s += 1
                dp[x][y] = min(dp[x][y], s)
        # Top to Bottom Traversal of Grid
        for x in range(n):
            s = 0
            for y in range(n):
                if grid[y][x] == 0:
                    s = 0
                else:
                    s += 1
                dp[y][x] = min(dp[y][x], s)
        # Bottom to Top Traversal of Grid
        for x in range(n):
            s = 0
            for y in range(n-1, -1, -1):
                if grid[y][x] == 0:
                    s = 0
                else:
                    s += 1
                dp[y][x] = min(dp[y][x], s)

        # Finding largest k-order
        ans = 0
        for x in range(n):
            for y in range(n):
                ans = max(ans, dp[x][y])
        return ans


def main():
    n = 5
    mines = [[4, 2]]
    assert Solution().orderOfLargestPlusSign(n, mines) == 2

    n = 1
    mines = [[0, 0]]
    assert Solution().orderOfLargestPlusSign(n, mines) == 0


if __name__ == '__main__':
    main()
