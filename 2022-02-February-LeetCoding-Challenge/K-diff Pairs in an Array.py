# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ''' Hashmap based O(n) solution. '''
        freq = Counter(nums)
        count = 0
        if k == 0:
            # Pairs of equal numbers, check if frequency > 1
            for val in freq.values():
                if val > 1:
                    count += 1
        else:
            # For number, check if number+k exists
            for key in freq.keys():
                if key+k in freq:
                    count += 1
        return count


def main():
    nums, k = [3, 1, 4, 1, 5], 2
    assert Solution().findPairs(nums, k) == 2

    nums, k = [1, 2, 3, 4, 5], 1
    assert Solution().findPairs(nums, k) == 4


if __name__ == '__main__':
    main()
