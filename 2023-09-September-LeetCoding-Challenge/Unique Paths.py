from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache(None)
        def dfs(m: int, n: int) -> int:
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1
            return dfs(m-1, n) + dfs(m, n-1)

        return dfs(m-1, n-1)


def main():
    m, n = 3, 7
    assert Solution().uniquePaths(m, n) == 28

    m, n = 3, 2
    assert Solution().uniquePaths(m, n) == 3


if __name__ == '__main__':
    main()
