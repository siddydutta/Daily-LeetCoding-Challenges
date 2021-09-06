# -*- coding: utf-8 -*-
from math import inf
from typing import List


class NaiveSolution:
    ''' Backtracking approach to get all possible partitions. '''
    def minCut(self, s: str) -> int:
        def dfs(substring: str, path: List[str]) -> None:
            if not substring:
                partitions.append(path.copy())  # Base case
                return
            for i in range(1, len(substring)+1):
                if substring[:i] == substring[:i][::-1]:
                    path.append(substring[:i])
                    dfs(substring[i:], path)
                    path.pop()  # To backtrack

        partitions = list()
        dfs(s, list())
        min_length = inf
        for partition in partitions:
            min_length = min(min_length, len(partition))
        return min_length-1


class Solution:
    ''' Dynamic programming solution. '''
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0  # String is palindrome, no cuts required

        n = len(s)
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1  # Direct solution if min cut is 1

        dp = [-1] + [inf] * (n)
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    dp[j+1] = min(dp[j+1], dp[i]+1)
        return dp[-1]


def main():
    s = "a"
    assert Solution().minCut(s) == 0

    s = "aab"
    assert Solution().minCut(s) == 1

    s = "abababcababab"
    assert Solution().minCut(s) == 4


if __name__ == '__main__':
    main()
