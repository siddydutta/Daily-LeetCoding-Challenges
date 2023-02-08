# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end, curr_max = 0, 0
        for i in range(len(nums)-1):
            curr_max = max(curr_max, i+nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_max
        return jumps


def main():
    nums = [2, 3, 1, 1, 4]
    assert Solution().jump(nums) == 2

    nums = [2, 3, 0, 1, 4]
    assert Solution().jump(nums) == 2


if __name__ == '__main__':
    main()
