from heapq import heapify, heappop, heappush
from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)
        for _ in range(k):
            max_pile = -heappop(heap)
            heappush(heap, -isqrt(max_pile))
        return -sum(heap)


def main():
    gifts = [25, 64, 9, 4, 100]
    k = 4
    assert Solution().pickGifts(gifts, k) == 29

    gifts = [1, 1, 1, 1]
    k = 4
    assert Solution().pickGifts(gifts, k) == 4


if __name__ == '__main__':
    main()
