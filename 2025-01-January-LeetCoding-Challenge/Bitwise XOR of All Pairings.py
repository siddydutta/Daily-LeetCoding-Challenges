from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0
        if len(nums1) & 1 != 0:
            x = reduce(xor, nums2)
        if len(nums2) & 1 != 0:
            x ^= reduce(xor, nums1)
        return x


def main():
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    assert Solution().xorAllNums(nums1, nums2) == 13

    nums1 = [1, 2]
    nums2 = [3, 4]
    assert Solution().xorAllNums(nums1, nums2) == 0


if __name__ == '__main__':
    main()
