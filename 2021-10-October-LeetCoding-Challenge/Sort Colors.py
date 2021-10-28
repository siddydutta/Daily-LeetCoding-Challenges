# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution1:
    ''' Straightforward solution without using sort. '''
    def sortColors(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        idx = 0
        for color in range(3):
            count = freq.get(color, 0)
            for i in range(count):
                nums[idx] = color
                idx += 1
        return nums


class Solution2:
    ''' Two pointer based solution. '''
    def sortColors(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1  # left for 0, right for 2
        ptr = 0

        while ptr <= right:
            if nums[ptr] == 0:
                nums[ptr], nums[left] = nums[left], nums[ptr]
                ptr += 1
                left += 1
            elif nums[ptr] == 1:
                ptr += 1  # No swap, maintain position
            elif nums[ptr] == 2:
                nums[ptr], nums[right] = nums[right], nums[ptr]
                right -= 1

        return nums


def main():
    for obj in [Solution1(), Solution2()]:
        nums = [2, 0, 2, 1, 1, 0]
        assert obj.sortColors(nums) == sorted(nums)

        nums = [2, 0, 1]
        assert obj.sortColors(nums) == sorted(nums)

        nums = [0]
        assert obj.sortColors(nums) == sorted(nums)

        nums = [1]
        assert obj.sortColors(nums) == sorted(nums)


if __name__ == '__main__':
    main()
