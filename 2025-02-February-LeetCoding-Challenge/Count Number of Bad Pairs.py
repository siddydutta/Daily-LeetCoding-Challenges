from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        total_pairs = (n * (n-1)) // 2
        good_pairs = 0
        for i in range(n):
            key = nums[i] - i
            good_pairs += freq[key]
            freq[key] += 1
        return total_pairs - good_pairs


def main():
    nums = [4, 1, 3, 3]
    assert Solution().countBadPairs(nums) == 5

    nums = [1, 2, 3, 4, 5]
    assert Solution().countBadPairs(nums) == 0


if __name__ == '__main__':
    main()
