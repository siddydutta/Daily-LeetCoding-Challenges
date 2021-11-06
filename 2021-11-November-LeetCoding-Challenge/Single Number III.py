# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class NotSolution:
    ''' Simple pythonic solution. '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [key for key, value in Counter(nums).items() if value == 1]


class Solution:
    '''
    Solution based on bit manipulation.
    Time Complexity: O(n)  Space Complexity: O(1)
    '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        # First pass XORs all elements, the resultant xor is the XOR of
        # the two elements that exist only once
        for num in nums:
            xor ^= num
        xor &= -xor  # Find an arbitrary set bit

        # Numbers can be divided into two groups
        # One with arbitrary bit set and another with the same bit unset
        # Second pass ensures the two distinct elements are separated into
        # the two groups and XOR ensures duplicate elements are eliminated
        res = [0, 0]
        for num in nums:
            if num & xor == 0:
                res[0] ^= num  # Group with bit unset
            else:
                res[1] ^= num  # Group with bit set

        return res


def main():
    nums = [1, 2, 1, 3, 2, 5]
    assert set(Solution().singleNumber(nums)) == set([3, 5])

    nums = [-1, 0]
    assert set(Solution().singleNumber(nums)) == set([-1, 0])

    nums = [0, 1]
    assert set(Solution().singleNumber(nums)) == set([0, 1])


if __name__ == '__main__':
    main()
