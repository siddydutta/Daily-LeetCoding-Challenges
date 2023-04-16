# -*- coding: utf-8 -*-
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        count = [Counter(word) for word in zip(*words)]

        @lru_cache
        def dfs(i: int, j: int) -> int:
            if i == len(target):
                return 1
            if j == len(words[0]):
                return 0
            return (dfs(i, j+1) + dfs(i+1, j+1)*count[j][target[i]])

        return dfs(0, 0) % int(1e9+7)


def main():
    words, target = ["acca", "bbbb", "caca"], "aba"
    assert Solution().numWays(words, target) == 6

    words, target = ["abba", "baab"], "bab"
    assert Solution().numWays(words, target) == 4


if __name__ == '__main__':
    main()
