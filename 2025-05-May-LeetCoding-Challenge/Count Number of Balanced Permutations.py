from functools import lru_cache
from collections import Counter
from math import comb


class Solution:
    MOD = 10**9 + 7

    def countBalancedPermutations(self, num: str) -> int:
        count = Counter(map(int, num))
        total = sum(map(int, num))

        @lru_cache(None)
        def dfs(i: int, odd: int, even: int, balance: int) -> int:
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0

            res = 0
            for j in range(0, count[i] + 1):
                res += comb(odd, j) * \
                    comb(even, count[i] - j) * \
                    dfs(i - 1, odd - j, even - count[i] + j, balance - i * j)
            return res % self.MOD

        return 0 if total % 2 else dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)


def main():
    num = '123'
    assert Solution().countBalancedPermutations(num) == 2

    num = '112'
    assert Solution().countBalancedPermutations(num) == 1

    num = '12345'
    assert Solution().countBalancedPermutations(num) == 0


if __name__ == '__main__':
    main()
