# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Simple array based solution.
    Water is collected if there is a higher block on both left and right sides.
    Time Complexity: O(n)
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Edge case
        if n <= 2:
            return 0  # No water trapped

        left_max = height[0]
        left_high = [left_max]  # The highest block height on the left
        for i in range(1, n):
            if height[i] > left_max:
                left_max = height[i]
            left_high.append(left_max)

        right_max = height[n-1]
        right_high = [right_max]  # The highest block height on the right
        for i in range(n-2, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            right_high.insert(0, right_max)

        # The amount of water trapped is the minimum of left and right
        # highest blocks, subtracted by the current block height.
        ans = 0
        for i in range(n):
            ans += (min(left_high[i], right_high[i]) - height[i])
        return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert Solution().trap(height) == 6

    height = [3, 1, 2, 4, 0, 1, 3, 2]
    assert Solution().trap(height) == 8

    height = [4, 2, 0, 3, 2, 5]
    assert Solution().trap(height) == 9


if __name__ == '__main__':
    main()
