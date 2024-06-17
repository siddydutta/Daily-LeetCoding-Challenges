from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0  # number of patches
        miss = 1  # next missing number in range
        i = 0  # index pointer
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # can form all numbers to until next miss
                i += 1
            else:
                miss += miss  # add the miss number itself
                patch += 1
        return patch


def main():
    nums = [1, 3]
    n = 6
    assert Solution().minPatches(nums, n) == 1

    nums = [1, 5, 10]
    n = 20
    assert Solution().minPatches(nums, n) == 2


if __name__ == '__main__':
    main()
