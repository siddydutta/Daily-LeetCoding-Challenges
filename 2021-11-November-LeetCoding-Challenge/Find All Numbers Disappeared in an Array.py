# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num)-1  # Since arrays are 0-indexed
            nums[idx] = -abs(nums[idx])  # Make visited indices negative

        # Return indices containing positive numbers
        return [idx+1 for idx, num in enumerate(nums) if num > 0]


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    assert Solution().findDisappearedNumbers(nums) == [5, 6]

    nums = [1, 1]
    assert Solution().findDisappearedNumbers(nums) == [2]


if __name__ == '__main__':
    main()
