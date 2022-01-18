# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ptr = 0
        while ptr < len(flowerbed) and n > 0:
            if flowerbed[ptr] != 0:
                # Non-empty plot
                ptr += 1
                continue
            # Get previous and next plots, 0 if doesn't exist
            previous = flowerbed[ptr-1] if ptr != 0 else 0
            nextt = flowerbed[ptr+1] if ptr != len(flowerbed)-1 else 0
            if previous == 0 and nextt == 0:
                # Adjacent plots are empty
                flowerbed[ptr] = 1
                n -= 1
                ptr += 2  # Since next plot cannot be used
            else:
                ptr += 1
        return n == 0  # If all flowers are planted


def main():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    assert Solution().canPlaceFlowers(flowerbed, n)

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    assert not Solution().canPlaceFlowers(flowerbed, n)


if __name__ == '__main__':
    main()
