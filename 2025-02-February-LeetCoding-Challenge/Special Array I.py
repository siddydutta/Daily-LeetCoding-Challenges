from itertools import pairwise
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return not any(i & 1 == j & 1 for i, j in pairwise(nums))


def main():
    nums = [1]
    assert Solution().isArraySpecial(nums) is True

    nums = [2, 1, 4]
    assert Solution().isArraySpecial(nums) is True

    nums = [4, 3, 1, 6]
    assert Solution().isArraySpecial(nums) is False


if __name__ == '__main__':
    main()
