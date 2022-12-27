# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int],
                    additionalRocks: int) -> int:
        remaining = sorted([c - r for c, r in zip(capacity, rocks)])
        bags = 0
        for current in remaining:
            if additionalRocks >= current:
                additionalRocks -= current
                bags += 1
            else:
                break
        return bags


def main():
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2
    assert Solution().maximumBags(capacity, rocks, additionalRocks) == 3

    capacity = [10, 2, 2]
    rocks = [2, 2, 0]
    additionalRocks = 100
    assert Solution().maximumBags(capacity, rocks, additionalRocks) == 3


if __name__ == '__main__':
    main()
