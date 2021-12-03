# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ''' Dynamic programming based solution. '''
        # Min is also maintained to account for negative number multiplication
        prev_max = prev_min = ans = nums[0]

        for i in range(1, len(nums)):
            # For every number, try to update max and min products
            curr_max = max(max(prev_max*nums[i], prev_min*nums[i]), nums[i])
            curr_min = min(min(prev_max*nums[i], prev_min*nums[i]), nums[i])
            ans = max(ans, curr_max)
            prev_max, prev_min = curr_max, curr_min

        return ans


def main():
    nums = [2, 3, -2, 4]
    assert Solution().maxProduct(nums) == 6

    nums = [-2, 0, -1]
    assert Solution().maxProduct(nums) == 0


if __name__ == '__main__':
    main()
