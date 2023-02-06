# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for n1, n2 in zip(nums[:n], nums[n:]):
            arr += [n1, n2]
        return arr


def main():
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    assert Solution().shuffle(nums, n) == [2, 3, 5, 4, 1, 7]

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    assert Solution().shuffle(nums, n) == [1, 4, 2, 3, 3, 2, 4, 1]

    nums = [1, 1, 2, 2]
    n = 2
    assert Solution().shuffle(nums, n) == [1, 2, 1, 2]


if __name__ == '__main__':
    main()
