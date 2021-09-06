# -*- coding: utf-8 -*-
class Solution:
    '''
    Bottom-up dynamic programming solution.
    Time Complexity: O(n)
    '''
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            prev_one = int(s[i-1])  # 12 -> 2
            prev_two = int(s[i-2] + s[i-1])  # 12 -> 12
            if prev_one >= 1:
                dp[i] += dp[i-1]  # If prev one is valid
            if prev_two >= 10 and prev_two <= 26:
                dp[i] += dp[i-2]  # If prev two is valid

        return dp[-1]


def main():
    s = "12"
    assert Solution().numDecodings(s) == 2

    s = "226"
    assert Solution().numDecodings(s) == 3

    s = "0"
    assert Solution().numDecodings(s) == 0

    s = "06"
    assert Solution().numDecodings(s) == 0


if __name__ == '__main__':
    main()
