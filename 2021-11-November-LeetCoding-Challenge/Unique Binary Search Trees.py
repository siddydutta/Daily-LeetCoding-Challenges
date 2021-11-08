# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    ''' Recursive solution. '''
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def recursive(n):
            if n <= 1:
                return 1
            s = 0
            for i in range(1, n+1):
                # n different left subtrees * n different right subtrees
                s += recursive(i-1) * recursive(n-i)
            return s

        return recursive(n)


def main():
    n = 3
    assert Solution().numTrees(n) == 5

    n = 1
    assert Solution().numTrees(n) == 1

    n = 19
    assert Solution().numTrees(n) == 1767263190


if __name__ == '__main__':
    main()
