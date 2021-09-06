# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Using binary search to find deflection point.
    Time Complexity: O(log n)
    '''
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                # Previous element is greater, so current element is min
                return nums[mid]

            # Compare with last (or first) element to move towards min
            if nums[mid] > nums[-1]:
                left = mid + 1   # Last element is smaller, so move right
            elif nums[mid] < nums[-1]:
                right = mid - 1  # Last element is greater, so move left

        return  # Dummy return


def main():
    nums = [3, 4, 5, 1, 2]
    assert Solution().findMin(nums) == min(nums)

    nums = [4, 5, 6, 7, 0, 1, 2]
    assert Solution().findMin(nums) == min(nums)

    nums = [11, 13, 15, 17]
    assert Solution().findMin(nums) == min(nums)

    nums = [2, 3, 4, 5, 1]
    assert Solution().findMin(nums) == min(nums)


if __name__ == '__main__':
    main()
