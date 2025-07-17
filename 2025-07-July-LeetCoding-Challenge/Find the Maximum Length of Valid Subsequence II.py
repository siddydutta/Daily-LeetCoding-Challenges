class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        result = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                result = max(result, dp[prev][num])
        return result


def main():
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert Solution().maximumLength(nums, k) == 5

    nums = [1, 4, 2, 3, 1, 4]
    k = 3
    assert Solution().maximumLength(nums, k) == 4


if __name__ == '__main__':
    main()
