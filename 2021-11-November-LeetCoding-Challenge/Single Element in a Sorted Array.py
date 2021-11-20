# -*- coding: utf-8 -*-
from typing import List


class NotSolution:
    '''
    Bit manipulation based solution.
    Time Complexity: O(n)    Space Complexity: O(1)
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor


class Solution:
    '''
    Binary search based solution.
    Time Complexity: O(n)    Space Complexity: O(1)
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or \
                    (mid % 2 != 0 and nums[mid] == nums[mid-1]):
                # If pairs valid so far, move to next pair
                left = mid + 1
            else:
                right = mid
        return nums[left]


def main():
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    assert Solution().singleNonDuplicate(nums) == 2

    nums = [3, 3, 7, 7, 10, 11, 11]
    assert Solution().singleNonDuplicate(nums) == 10


if __name__ == '__main__':
    main()
