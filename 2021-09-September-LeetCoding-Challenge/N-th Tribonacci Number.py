# -*- coding: utf-8 -*-
class Solution:
    ''' Dynamic programming solution. '''
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1] + [None] * (n-3+1)
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]


def main():
    n = 4
    assert Solution().tribonacci(n) == 4

    n = 25
    assert Solution().tribonacci(n) == 1389537


if __name__ == '__main__':
    main()
