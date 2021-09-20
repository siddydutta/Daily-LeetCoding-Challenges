# -*- coding: utf-8 -*-
class Solution:
    ''' Dynamic Programming solution. '''
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[1] * (m+1)] + [[0 for _ in range(m+1)] for _ in range(n)]

        for i, ch1 in enumerate(t):
            for j, ch2 in enumerate(s):
                if ch1 == ch2:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]

        return dp[-1][-1]


def main():
    s = "rabbbit"
    t = "rabbit"
    assert Solution().numDistinct(s, t) == 3

    s = "babgbag"
    t = "bag"
    assert Solution().numDistinct(s, t) == 5


if __name__ == '__main__':
    main()
