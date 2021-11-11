# -*- coding: utf-8 -*-
from itertools import accumulate
from typing import List


class Solution:
    ''' Prefix sum based solution. '''
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = min(accumulate(nums))
        return 1-min(accumulate(nums)) if min_prefix_sum < 0 else 1
        # return max(1-min(accumulate(nums)), 1)


def main():
    nums = [-3, 2, -3, 4, 2]
    assert Solution().minStartValue(nums) == 5

    nums = [1, 2]
    assert Solution().minStartValue(nums) == 1

    nums = [1, -2, -3]
    assert Solution().minStartValue(nums) == 5


if __name__ == '__main__':
    main()
