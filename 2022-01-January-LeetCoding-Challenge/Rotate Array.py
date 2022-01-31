# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        ''' Straightforward, Pythonic-solution. '''
        k %= len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums


class Solution2:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        ''' Recursive solution. '''
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n  # Number of rotations
        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)
        return nums


def main():
    for obj in [Solution1(), Solution2()]:
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        assert obj.rotate(nums, k) == [5, 6, 7, 1, 2, 3, 4]

        nums = [-1, -100, 3, 99]
        k = 2
        assert obj.rotate(nums, k) == [3, 99, -1, -100]


if __name__ == '__main__':
    main()
