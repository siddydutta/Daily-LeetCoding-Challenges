# -*- coding: utf-8 -*-
class Solution:
    def numTilings(self, n: int) -> int:
        ''' Dynamic programming solution. '''
        mod = 10**9 + 7
        dp = [0, 1, 2, 5] + [0]*(n-3)

        for i in range(4, n+1):
            dp[i] = 2*dp[i-1] + dp[i-3]  # Recurrence relation
            dp[i] %= mod

        return dp[n]


def main():
    n = 3
    assert Solution().numTilings(n) == 5

    n = 1000
    assert Solution().numTilings(n) == 979232805


if __name__ == '__main__':
    main()
