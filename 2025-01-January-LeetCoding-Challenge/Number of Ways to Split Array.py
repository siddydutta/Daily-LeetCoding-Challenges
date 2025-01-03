from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum, total_sum = 0, sum(nums)
        valid_splits = 0
        for num in nums[:-1]:
            prefix_sum += num
            if prefix_sum >= total_sum - prefix_sum:
                valid_splits += 1
        return valid_splits


def main():
    nums = [10, 4, -8, 7]
    assert Solution().waysToSplitArray(nums) == 2

    nums = [2, 3, 1, 0]
    assert Solution().waysToSplitArray(nums) == 2


if __name__ == '__main__':
    main()
