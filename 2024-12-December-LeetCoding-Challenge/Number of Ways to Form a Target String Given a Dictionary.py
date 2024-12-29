from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        count = [Counter() for _ in range(len(words[0]))]
        for word in words:
            for idx, ch in enumerate(word):
                count[idx][ch] += 1

        @lru_cache(None)
        def dfs(i: int = 0, j: int = 0) -> int:
            if i == len(target):
                return 1
            if j == len(words[0]):
                return 0
            return (dfs(i, j+1) + dfs(i+1, j+1) * count[j][target[i]]) % int(1e9 + 7)

        return dfs()


def main():
    words = ['acca', 'bbbb', 'caca']
    target = 'aba'
    assert Solution().numWays(words, target) == 6

    words = ['abba', 'baab']
    target = 'bab'
    assert Solution().numWays(words, target) == 4


if __name__ == '__main__':
    main()
