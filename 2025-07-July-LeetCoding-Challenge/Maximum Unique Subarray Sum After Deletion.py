class Solution:
    def maxSum(self, nums: list[int]) -> int:
        total, max_ = 0, float('-inf')
        seen = set()
        for num in nums:
            if num > 0 and num not in seen:
                total += num
                seen.add(num)
            max_ = max(max_, num)
        return total if total != 0 else max_


def main():
    nums = [1, 2, 3, 4, 5]
    assert Solution().maxSum(nums) == 15

    nums = [1, 1, 0, 1, 1]
    assert Solution().maxSum(nums) == 1

    nums = [1, 2, -1, -2, 1, 0, -1]
    assert Solution().maxSum(nums) == 3


if __name__ == '__main__':
    main()
