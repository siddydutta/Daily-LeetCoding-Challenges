# -*- coding: utf-8 -*-
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        for _ in range(k):
            heapreplace(piles, piles[0] // 2)
        return -sum(piles)


def main():
    piles = [5, 4, 9]
    k = 2
    assert Solution().minStoneSum(piles, k) == 12

    piles = [4, 3, 6, 7]
    k = 3
    assert Solution().minStoneSum(piles, k) == 12


if __name__ == '__main__':
    main()
