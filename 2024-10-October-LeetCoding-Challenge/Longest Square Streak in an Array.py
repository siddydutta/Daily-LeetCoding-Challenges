from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        max_num = nums[0]
        dp = [0] * (max_num+1)
        for num in nums:
            dp[num] = 1
            if num*num <= max_num:
                dp[num] += dp[num*num]
        return res if (res := max(dp)) >= 2 else -1


def main():
    nums = [4, 3, 6, 16, 8, 2]
    assert Solution().longestSquareStreak(nums) == 3

    nums = [2, 3, 5, 6, 7]
    assert Solution().longestSquareStreak(nums) == -1


if __name__ == '__main__':
    main()
