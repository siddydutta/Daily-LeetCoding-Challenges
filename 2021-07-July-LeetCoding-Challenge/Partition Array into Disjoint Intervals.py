# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Time Complexity: O(n) '''
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = all_max = nums[0]
        ptr_index = 0  # Partition pointer
        for i in range(len(nums)):
            all_max = max(all_max, nums[i])
            if nums[i] < left_max:
                # Condition for including in left sub array
                ptr_index = i
                left_max = all_max
        return ptr_index + 1  # Number of elements


def main():
    obj = Solution()
    nums = [5, 0, 3, 8, 6]
    assert obj.partitionDisjoint(nums) == 3
    nums = [1, 1, 1, 0, 6, 12]
    assert obj.partitionDisjoint(nums) == 4
    nums = [1, 1]
    assert obj.partitionDisjoint(nums) == 1
    nums = [90, 47, 69, 10, 43, 92, 31, 73, 61, 97]
    assert obj.partitionDisjoint(nums) == 9


if __name__ == '__main__':
    main()
