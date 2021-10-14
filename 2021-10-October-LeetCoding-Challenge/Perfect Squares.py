# -*- coding: utf-8 -*-
from math import inf


class Solution:
    ''' Dynamic programming solution. '''
    def numSquares(self, n: int) -> int:
        dp = [None for _ in range(n+1)]
        dp[0], dp[1] = 0, 1  # Initial answers

        for i in range(2, n+1):
            min_ans = inf
            j = 1  # Possible squares, giving smaller answers
            while i - j*j >= 0:
                # If candidate answer, update minimum
                min_ans = min(min_ans, dp[i-j*j] + 1)
                j += 1
            dp[i] = min_ans

        return dp[n]


def main():
    n = 12
    assert Solution().numSquares(n) == 3

    n = 13
    assert Solution().numSquares(n) == 2


if __name__ == '__main__':
    main()
