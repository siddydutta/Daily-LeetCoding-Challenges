# -*- coding: utf-8 -*-
class Solution:
    def findIntegers(self, n: int) -> int:
        upper_bin = bin(n+1)[2:]
        length = len(upper_bin)

        # Create fibonacci series
        dp = [1, 2] + [0]*(length-2)
        for i in range(2, length):
            dp[i] = dp[i-1] + dp[i-2]

        flag = False  # To check for consecutive ones
        ans = 0
        for i in range(length):
            if upper_bin[i] == '0':
                continue
            if flag:
                break
            if i > 0 and upper_bin[i-1] == '1':
                flag = True
            ans += dp[-i-1]

        return ans


def main():
    assert Solution().findIntegers(5) == 5
    assert Solution().findIntegers(12) == 8
    assert Solution().findIntegers(10**9) == 2178309


if __name__ == '__main__':
    main()
