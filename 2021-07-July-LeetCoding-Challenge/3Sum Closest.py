# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    ''' Time Complexity: O(n^2) '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf  # Minimum difference to target
        sum_value = 0   # Sum value that gives the above minimum difference

        for i in range(n):
            first, last = i+1, n-1  # Two numbers with i
            while first < last:
                current_sum = nums[i] + nums[first] + nums[last]  # 3 Sum
                difference = abs(target - current_sum)

                if difference < min_diff:
                    # Current sum is closer to target
                    min_diff = difference
                    sum_value = current_sum

                # Update indices for next three
                if current_sum < target:
                    first += 1  # Need a bigger number to reach target
                else:
                    last -= 1  # Need a smaller number to reach target

        return sum_value


def main():
    nums = [-1, 2, 1, -4]
    target = 1
    assert Solution().threeSumClosest(nums, target) == 2


if __name__ == '__main__':
    main()
