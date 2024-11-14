from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            s = 0
            for q in quantities:
                s += ceil(q / mid)
            if s > n:
                left = mid + 1
            else:
                right = mid
        return left


def main():
    n = 6
    quantities = [11, 6]
    assert Solution().minimizedMaximum(n, quantities) == 3

    n = 7
    quantities = [15, 10, 10]
    assert Solution().minimizedMaximum(n, quantities) == 5

    n = 1
    quantities = [100000]
    assert Solution().minimizedMaximum(n, quantities) == 100000


if __name__ == '__main__':
    main()
