# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' Straightforward pointer based solution. '''
        ptr = 2
        while ptr < len(nums):
            if nums[ptr] == nums[ptr-2]:
                nums.pop(ptr)
            else:
                ptr += 1
        return ptr


def main():
    nums = [1, 1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(nums) == 5

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert Solution().removeDuplicates(nums) == 7


if __name__ == '__main__':
    main()
