from math import comb


class Solution:
    MOD = 10**9 + 7

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return (comb(n - 1, k) * m * pow(m - 1, n - k - 1, self.MOD)) % self.MOD


def main():
    n = 3
    m = 2
    k = 1
    assert Solution().countGoodArrays(n, m, k) == 4

    n = 4
    m = 2
    k = 2
    assert Solution().countGoodArrays(n, m, k) == 6


if __name__ == '__main__':
    main()
