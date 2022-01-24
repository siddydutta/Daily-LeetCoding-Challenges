# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def compute_hours(self, piles: List[int], k: int) -> int:
        ''' Return hours required to eat all bananas at rate k. '''
        hours = int()
        for pile in piles:
            hours += pile // k
            if pile % k != 0:
                hours += 1  # Remainder bananas
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ''' Binary search based solution. '''
        low, high = 1, max(piles)
        while low <= high:
            K = low + ((high-low) // 2)  # Rate of eating bananas
            if self.compute_hours(piles, K) <= h:
                high = K - 1
            else:
                low = K + 1
        return low


def main():
    piles = [3, 6, 7, 11]
    h = 8
    assert Solution().minEatingSpeed(piles, h) == 4

    piles = [30, 11, 23, 4, 20]
    h = 5
    assert Solution().minEatingSpeed(piles, h) == 30

    piles = [30, 11, 23, 4, 20]
    h = 6
    assert Solution().minEatingSpeed(piles, h) == 23


if __name__ == '__main__':
    main()
