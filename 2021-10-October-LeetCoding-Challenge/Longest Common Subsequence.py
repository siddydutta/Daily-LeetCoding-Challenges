# -*- coding: utf-8 -*-
from functools import lru_cache


class RecursiveSolution:
    '''
    Recursive solution with memoization.
    Time Complexity: O(m*n)
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def lcs(i: int, j: int) -> int:
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                return 1 + lcs(i+1, j+1)
            else:
                return max(lcs(i+1, j), lcs(i, j+1))

        return lcs(0, 0)


class DPSolution:
    '''
    Dynamic programming solution.
    dP[i][j] represents the longest common subsequence of
    text1[0 ... i] & text2[0 ... j].
    Time Complexity: O(m*n)
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


def main():
    for obj in [RecursiveSolution(), DPSolution()]:
        text1 = "abcde"
        text2 = "ace"
        assert obj.longestCommonSubsequence(text1, text2) == 3
    
        text1 = "abc"
        text2 = "abc"
        assert obj.longestCommonSubsequence(text1, text2) == 3
    
        text1 = "abc"
        text2 = "def"
        assert obj.longestCommonSubsequence(text1, text2) == 0


if __name__ == '__main__':
    main()
