# -*- coding: utf-8 -*-
from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ''' Straightfoward Pythonic solution. '''
        power_set = list()
        for length in range(0, len(nums)+1):
            power_set += list(combinations(nums, length))
        return power_set


def main():
    nums = [1, 2, 3]
    assert Solution().subsets(nums) == [(), (1,), (2,), (3,), (1, 2),
                                        (1, 3), (2, 3), (1, 2, 3)]

    nums = [0]
    assert Solution().subsets(nums) == [(), (0,)]


if __name__ == '__main__':
    main()
