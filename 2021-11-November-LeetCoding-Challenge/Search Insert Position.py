# -*- coding: utf-8 -*-
from bisect import bisect_left
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ''' Binary search solution. '''
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class NotSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ''' Pythonic solution. '''
        return bisect_left(nums, target)


def main():
    nums = [1, 3, 5, 6]
    target = 5
    assert Solution().searchInsert(nums, target) == 2

    nums = [1, 3, 5, 6]
    target = 2
    assert Solution().searchInsert(nums, target) == 1

    nums = [1, 3, 5, 6]
    target = 7
    assert Solution().searchInsert(nums, target) == 4

    nums = [1, 3, 5, 6]
    target = 0
    assert Solution().searchInsert(nums, target) == 0

    nums = [1]
    target = 0
    assert Solution().searchInsert(nums, target) == 0


if __name__ == '__main__':
    main()
