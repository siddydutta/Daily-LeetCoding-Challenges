# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while (first <= last):
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return first


def main():
    nums, target = [1, 3, 5, 6], 5
    assert Solution().searchInsert(nums, target) == 2

    nums, target = [1, 3, 5, 6], 2
    assert Solution().searchInsert(nums, target) == 1

    nums, target = [1, 3, 5, 6], 7
    assert Solution().searchInsert(nums, target) == 4


if __name__ == '__main__':
    main()
