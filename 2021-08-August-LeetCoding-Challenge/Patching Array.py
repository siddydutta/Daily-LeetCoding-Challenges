# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Time Complexity : O(n) '''
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0  # Number of patches
        miss = 1  # Next missing number in range
        i = 0  # Index pointer
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # Can form all numbers to until next miss
                i += 1
            else:
                miss += miss  # Add the miss number itself
                patch += 1
        return patch


def main():
    nums = [1, 3]
    n = 6
    assert Solution().minPatches(nums, n) == 1

    nums = [1, 5, 10]
    n = 20
    assert Solution().minPatches(nums, n) == 2

    nums = list(range(1, 1001))
    n = 5
    assert Solution().minPatches(nums, n) == 0


if __name__ == '__main__':
    main()
