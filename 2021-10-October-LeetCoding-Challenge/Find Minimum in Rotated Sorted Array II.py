# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Binary search solution. '''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2  # mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # Smaller element is to the right
            elif nums[mid] < nums[right]:
                right = mid  # Smaller element is to the left
            else:  # nums[mid] == nums[right]
                right -= 1  # Move to smaller index of duplicate element
        return nums[left]  # nums[right] will also work


def main():
    nums = [1, 3, 5]
    assert Solution().findMin(nums) == 1

    nums = [2, 2, 2, 0, 1]
    assert Solution().findMin(nums) == 0

    nums = [1, 1]
    assert Solution().findMin(nums) == 1

    nums = [1]
    assert Solution().findMin(nums) == 1


if __name__ == '__main__':
    main()
