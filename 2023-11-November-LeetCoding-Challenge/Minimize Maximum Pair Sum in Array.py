from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for n1, n2 in zip(nums, reversed(nums)):
            max_sum = max(max_sum, (n1+n2))
        return max_sum


def main():
    nums = [3, 5, 2, 3]
    assert Solution().minPairSum(nums) == 7

    nums = [3, 5, 4, 2, 4, 6]
    assert Solution().minPairSum(nums) == 8


if __name__ == '__main__':
    main()
