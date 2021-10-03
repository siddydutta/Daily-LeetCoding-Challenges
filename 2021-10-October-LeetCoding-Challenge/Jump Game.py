# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Simple greedy solution.
    Update max possible index that can be reached based on current value.
    Time Complexity: O(n)
    '''
    def canJump(self, nums: List[int]) -> bool:
        max_next_index = 0
        for index, jump_length in enumerate(nums):
            if index > max_next_index:
                return False  # Crossed the index where we could reach max
            max_next_index = max(max_next_index, index+jump_length)
        return True


def main():
    nums = [2, 3, 1, 1, 4]
    assert Solution().canJump(nums)

    nums = [3, 2, 1, 0, 4]
    assert not Solution().canJump(nums)

    nums = [2, 0]
    assert Solution().canJump(nums)

    nums = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]
    assert Solution().canJump(nums)


if __name__ == '__main__':
    main()
