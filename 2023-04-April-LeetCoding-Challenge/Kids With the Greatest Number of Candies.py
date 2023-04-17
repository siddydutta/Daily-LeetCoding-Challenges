# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy+extra_candies >= max_candies for candy in candies]


def main():
    candies, extra_candies = [2, 3, 5, 1, 3], 3
    assert Solution().kidsWithCandies(candies, extra_candies) == [True, True, True, False, True]

    candies, extra_candies = [4, 2, 1, 1, 2], 1
    assert Solution().kidsWithCandies(candies, extra_candies) == [True, False, False, False, False]

    candies, extra_candies = [12, 1, 12], 10
    assert Solution().kidsWithCandies(candies, extra_candies) == [True, False, True]


if __name__ == '__main__':
    main()
