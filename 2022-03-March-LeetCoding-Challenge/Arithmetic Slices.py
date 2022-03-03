# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ''' Dynamic programming solution. '''
        n = len(nums)
        dp, count = [0]*n, 0

        for i in range(2, n):
            # Condition for arithmetic slices
            if nums[i-2]-nums[i-1] == nums[i-1]-nums[i]:
                dp[i] = dp[i-1] + 1
            count += dp[i]  # Update count at every num

        return count


def main():
    nums = [1, 2, 3, 4]
    assert Solution().numberOfArithmeticSlices(nums) == 3

    nums = [1]
    assert Solution().numberOfArithmeticSlices(nums) == 0


if __name__ == '__main__':
    main()
