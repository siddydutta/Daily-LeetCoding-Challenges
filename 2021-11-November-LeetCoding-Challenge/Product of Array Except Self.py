# -*- coding: utf-8 -*-
from itertools import accumulate
from operator import mul
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Simple Pythonic solution, using accumulate.
        Does not use the division operator.
        Time Complexity: O(n)    Space Complexity: O(n)
        '''
        lefts = [1] + list(accumulate(nums[:-1], mul))
        rights = list(accumulate(nums[1:][::-1], mul))[::-1] + [1]
        return [x*y for x, y in zip(lefts, rights)]


def main():
    nums = [1, 2, 3, 4]
    assert Solution().productExceptSelf(nums) == [24, 12, 8, 6]

    nums = [-1, 1, 0, -3, 3]
    assert Solution().productExceptSelf(nums) == [0, 0, 9, 0, 0]


if __name__ == '__main__':
    main()
