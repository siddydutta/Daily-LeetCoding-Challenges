# -*- coding: utf-8 -*-
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]  # create max-heap
        heapify(stones)
        while len(stones) > 1:
            y, x = heappop(stones), heappop(stones)
            if x != y:
                heappush(stones, y-x)
        return -stones[0] if stones else 0


def main():
    stones = [2, 7, 4, 1, 8, 1]
    assert Solution().lastStoneWeight(stones) == 1

    stones = [1]
    assert Solution().lastStoneWeight(stones) == 1


if __name__ == '__main__':
    main()
