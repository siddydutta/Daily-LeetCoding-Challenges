# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import List


class NotSolution:
    def maxCoins(self, nums: List[int]) -> int:
        ''' Top-down recursive solution leads to TLE. '''
        nums = [1] + nums + [1]  # Pad initial array
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            coins = 0
            for k in range(i+1, j):
                coins = max(coins,
                            nums[i]*nums[k]*nums[j] + dfs(i, k) + dfs(k, j))
            return coins
        return dfs(0, len(nums)-1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ''' Bottom-up dynamic programming solution. '''
        nums = [1] + nums + [1]  # Pad initial array
        n = len(nums)
        # dp[i][j] indicates max coins when subarray is nums[i:j+1]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for length in range(2, n):  # Length of subarray under computation
            for i in range(n-length):  # Starting index
                j = i + length  # Ending index
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j],
                                   nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])

        return dp[0][n-1]


def main():
    nums = [3, 1, 5, 8]
    assert Solution().maxCoins(nums) == 167

    nums = [1, 5]
    assert Solution().maxCoins(nums) == 10


if __name__ == '__main__':
    main()
