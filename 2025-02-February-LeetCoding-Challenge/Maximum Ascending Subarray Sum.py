from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum


def main():
    nums = [10, 20, 30, 5, 10, 50]
    assert Solution().maxAscendingSum(nums) == 65

    nums = [10, 20, 30, 40, 50]
    assert Solution().maxAscendingSum(nums) == 150

    nums = [12, 17, 15, 13, 10, 11, 12]
    assert Solution().maxAscendingSum(nums) == 33


if __name__ == '__main__':
    main()
