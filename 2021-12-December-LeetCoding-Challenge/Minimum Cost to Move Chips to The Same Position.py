# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ''' Math based solution. '''
        # Odd to odd and even to even moves are free
        # Odd to even or even to odd moves account for 1 cost
        # Determine whether to move all to a an odd position or even position
        parity = [chip % 2 == 0 for chip in position]
        return min(parity.count(1), parity.count(0))


def main():
    position = [1, 2, 3]
    assert Solution().minCostToMoveChips(position) == 1

    position = [2, 2, 2, 3, 3]
    assert Solution().minCostToMoveChips(position) == 2

    position = [1, 1000000000]
    assert Solution().minCostToMoveChips(position) == 1


if __name__ == '__main__':
    main()
