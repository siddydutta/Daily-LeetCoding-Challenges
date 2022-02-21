# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ''' Straightforward hashmap based solution. '''
        freq_map, req_occ = Counter(nums), len(nums) // 2
        for num, freq in freq_map.items():
            if freq > req_occ:
                return num


def main():
    nums = [3, 2, 3]
    assert Solution().majorityElement(nums) == 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    assert Solution().majorityElement(nums) == 2


if __name__ == '__main__':
    main()
