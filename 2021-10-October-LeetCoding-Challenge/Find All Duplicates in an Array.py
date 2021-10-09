# -*- coding: utf-8 -*-
from typing import List


class NotSolution:
    ''' Naive solution. Time Complexity: O(n). Space Complexity: O(n). '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen, repeated = set(), list()
        for num in nums:
            if num in seen:
                repeated.append(num)
            seen.add(num)
        return repeated
        # return list(filter((None).__ne__, [num if num in seen else seen.add(num) for num in nums]))


class Solution:
    '''
    Solution based on rearranging a number to its index.
    Time Complexity: O(n)
    Space Compleixty: O(1)
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            # If number doesn't belong in the index, swap with correct place
            while nums[idx] != nums[nums[idx]-1]:
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]
        # Return all numbers that do not match index
        return [num for idx, num in enumerate(nums, 1) if num != idx]


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    assert Solution().findDuplicates(nums) == [2, 3] or \
        Solution().findDuplicates(nums) == [3, 2]

    nums = [1, 1, 2]
    assert Solution().findDuplicates(nums) == [1]

    nums = [1]
    assert Solution().findDuplicates(nums) == []


if __name__ == '__main__':
    main()
