from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        inc = 0
        for i in range(1, len(nums)):
            need = max(nums[i-1] + 1, nums[i])
            inc += (need - nums[i])
            nums[i] = need
        return inc


def main():
    nums = [1, 2, 2]
    assert Solution().minIncrementForUnique(nums) == 1

    nums = [3, 2, 1, 2, 1, 7]
    assert Solution().minIncrementForUnique(nums) == 6


if __name__ == '__main__':
    main()
