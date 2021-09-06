# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Top-down dynamic programming approach.
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # Duplicate numbers need not be computed
        max_count = int()
        cache = dict()

        def dp(num):
            if num in cache:
                # Consecutive count for number already computed
                return cache.get(num)

            count = 1
            if num-1 in nums:
                # If num-1 is also present, compute num-1
                count += dp(num-1)

            cache[num] = count  # Store num's consecutive count in cache
            return count

        for num in nums:
            max_count = max(max_count, dp(num))
        return max_count


if __name__ == '__main__':
    obj = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    assert obj.longestConsecutive(nums) == 4

    obj = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert obj.longestConsecutive(nums) == 9
