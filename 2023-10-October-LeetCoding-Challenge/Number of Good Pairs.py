from collections import Counter
from math import comb
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        for group_count in freq.values():
            if group_count > 1:
                count += comb(group_count, 2)
        return count


def main():
    nums = [1, 2, 3, 1, 1, 3]
    assert Solution().numIdenticalPairs(nums) == 4

    nums = [1, 1, 1, 1]
    assert Solution().numIdenticalPairs(nums) == 6

    nums = [1, 2, 3]
    assert Solution().numIdenticalPairs(nums) == 0


if __name__ == '__main__':
    main()
