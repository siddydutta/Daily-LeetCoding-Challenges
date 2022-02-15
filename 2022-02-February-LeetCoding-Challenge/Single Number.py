# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' XOR based linear-time, constant space solution. '''
        xor = nums[0]
        for num in nums[1:]:
            xor ^= num  # Since x ^ x = 0
        return xor  # The num that remains has not been XOR-ed with itself


def main():
    nums = [2, 2, 1]
    assert Solution().singleNumber(nums) == 1

    nums = [4, 1, 2, 1, 2]
    assert Solution().singleNumber(nums) == 4

    nums = [1]
    assert Solution().singleNumber(nums) == 1


if __name__ == '__main__':
    main()
