# -*- coding: utf-8 -*-
from itertools import accumulate
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max([(s+i)//(i+1) for i, s in enumerate(accumulate(nums))])


def main():
    nums = [3, 7, 1, 6]
    assert Solution().minimizeArrayValue(nums) == 5

    nums = [10, 1]
    assert Solution().minimizeArrayValue(nums) == 10


if __name__ == '__main__':
    main()
