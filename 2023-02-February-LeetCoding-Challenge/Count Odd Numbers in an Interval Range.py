# -*- coding: utf-8 -*-
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


def main():
    low, high = 3, 7
    assert Solution().countOdds(low, high) == 3

    low, high = 8, 10
    assert Solution().countOdds(low, high) == 1


if __name__ == '__main__':
    main()
