# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def main():
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    assert Solution().search(nums, target) == 4

    nums, target = [-1, 0, 3, 5, 9, 12], 2
    assert Solution().search(nums, target) == -1


if __name__ == '__main__':
    main()
