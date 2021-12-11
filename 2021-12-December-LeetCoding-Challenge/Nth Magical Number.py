# -*- coding: utf-8 -*-
from math import gcd


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm = a*b / gcd(a, b)

        left, right = min(a, b), max(a, b) * n
        while left <= right:
            mid = (left + right) // 2
            curr = mid // a + mid // b - mid // lcm
            if curr == n:
                res = mid - min(mid % a, mid % b)
                return res % mod
            if curr < n:
                left = mid + 1
            else:
                right = mid - 1

        return left % mod


def main():
    n, a, b = 1, 2, 3
    assert Solution().nthMagicalNumber(n, a, b) == 2

    n, a, b = 4, 2, 3
    assert Solution().nthMagicalNumber(n, a, b) == 6

    n, a, b = 5, 2, 4
    assert Solution().nthMagicalNumber(n, a, b) == 10

    n, a, b = 3, 6, 4
    assert Solution().nthMagicalNumber(n, a, b) == 8


if __name__ == '__main__':
    main()
