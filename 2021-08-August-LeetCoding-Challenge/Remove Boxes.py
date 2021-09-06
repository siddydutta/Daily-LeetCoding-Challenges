# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import List


class Solution1:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dfs(left, right, streak):
            if left > right:
                return 0
            if left == right:
                return (streak+1) * (streak+1)
            if dp[left][right][streak] != 0:
                return dp[left][right][streak]

            points = dfs(left+1, right, 0) + ((streak+1) * (streak+1))
            for ptr in range(left+1, right+1):
                if boxes[left] == boxes[ptr]:
                    points = max(points, dfs(left+1, ptr-1, 0) +
                                 dfs(ptr, right, streak+1))
            dp[left][right][streak] = points
            return points

        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return dfs(0, n-1, 0)


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(left, right, streak):
            if left > right:
                return 0

            ptr = left
            count = 1
            while ptr < right and boxes[ptr] == boxes[ptr+1]:
                ptr += 1
                count += 1
            points = dfs(ptr+1, right, 0) + (count+streak)**2

            for i in range(ptr+1, right+1):
                if boxes[i] == boxes[ptr]:
                    points = max(points, dfs(ptr+1, i-1, 0) +
                                 dfs(i, right, count+streak))

            return points

        return dfs(0, len(boxes)-1, 0)


def main():
    boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    assert Solution().removeBoxes(boxes) == 23

    boxes = [1, 1, 1]
    assert Solution().removeBoxes(boxes) == 9

    boxes = [1]
    assert Solution().removeBoxes(boxes) == 1


if __name__ == '__main__':
    main()
