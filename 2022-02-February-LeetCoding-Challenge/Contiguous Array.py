# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ''' Hashtable and prefix sum based solution. '''
        table = {0: -1}  # Initial 0 starts from -1
        max_length, count = 0, 0
        for index, num in enumerate(nums):
            count = count - 1 if num == 0 else count + 1
            if count in table:
                max_length = max(max_length, index-table.get(count))
            else:
                table[count] = index
        return max_length


def main():
    nums = [0, 1]
    assert Solution().findMaxLength(nums) == 2

    nums = [0, 1, 0]
    assert Solution().findMaxLength(nums) == 2


if __name__ == '__main__':
    main()
