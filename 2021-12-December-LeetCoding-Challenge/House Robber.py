# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' Dynamic programming solution. '''
        if len(nums) == 1:
            return nums[0]  # Edge case

        dp = [None] * len(nums)
        # Recurrence relations
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # Either rob the second-last house and current house
            # or just keep the robbery from the previous house
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]


def main():
    nums = [1, 2, 3, 1]
    assert Solution().rob(nums) == 4

    nums = [2, 7, 9, 3, 1]
    assert Solution().rob(nums) == 12


if __name__ == '__main__':
    main()
