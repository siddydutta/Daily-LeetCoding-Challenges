# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ''' Solution based on monotonic stack. '''
        stack, ans = list(), int()
        for i, height in enumerate(heights + [0]):
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                ans = max(ans, h*w)
            stack.append(i)
        return ans


def main():
    heights = [2, 1, 5, 6, 2, 3]
    assert Solution().largestRectangleArea(heights) == 10

    heights = [2, 4]
    assert Solution().largestRectangleArea(heights) == 4


if __name__ == '__main__':
    main()
