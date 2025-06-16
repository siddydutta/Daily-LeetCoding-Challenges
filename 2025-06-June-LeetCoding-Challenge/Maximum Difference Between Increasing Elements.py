class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_so_far, max_diff = float('inf'), float('-inf')
        for num in nums:
            min_so_far = min(min_so_far, num)
            max_diff = max(max_diff, num - min_so_far)
        return max_diff if max_diff else -1


def main():
    nums = [7, 1, 5, 4]
    assert Solution().maximumDifference(nums) == 4

    nums = [9, 4, 3, 2]
    assert Solution().maximumDifference(nums) == -1

    nums = [1, 5, 2, 10]
    assert Solution().maximumDifference(nums) == 9


if __name__ == '__main__':
    main()
