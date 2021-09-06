# -*- coding: utf-8 -*-
class Solution:
    '''
    Bottom-up dynamic programming approach.
    dp[i][j] is the number of strings of length i+1 ending with j-th vowel.
    The total number of strings starting with a vowel is equal to the sum
    of the second last possible vowel(s).
    Time Complexity: O(n)
    '''
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * 5 for _ in range(n)]  # [a, e, i, o, u]

        # Base case for unit string length
        for j in range(5):
            dp[0][j] = 1

        # Reccurence relations for every vowel
        for i in range(1, n):
            # a follows after e, i, u
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % mod
            # e follows after a, i
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            # i follows after e, o
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod
            # o follows after i
            dp[i][3] = (dp[i-1][2]) % mod
            # u follows after i, o
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % mod

        return sum(dp[-1]) % mod


def main():
    obj = Solution()

    assert obj.countVowelPermutation(1) == 5
    assert obj.countVowelPermutation(2) == 10
    assert obj.countVowelPermutation(5) == 68


if __name__ == '__main__':
    main()
