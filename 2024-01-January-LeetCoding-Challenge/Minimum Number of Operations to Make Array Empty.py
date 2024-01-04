from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ops = 0
        for freq in counts.values():
            if freq == 1:
                return -1
            ops += ceil(freq / 3)
        return ops


def main():
    nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
    assert Solution().minOperations(nums) == 4

    nums = [2, 1, 2, 2, 3, 3]
    assert Solution().minOperations(nums) == -1


if __name__ == '__main__':
    main()
