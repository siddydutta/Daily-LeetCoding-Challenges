from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        prefix_sum = 0
        prefix_map = {0: -1}
        min_len = len(nums)
        for i, num in enumerate(nums):
            prefix_sum += num
            curr_remainder = prefix_sum % p
            needed_remainder = (curr_remainder - target) % p
            if needed_remainder in prefix_map:
                min_len = min(min_len, i - prefix_map[needed_remainder])
            prefix_map[curr_remainder] = i

        return min_len if min_len < len(nums) else -1


def main():
    nums = [3, 1, 4, 2]
    p = 6
    assert Solution().minSubarray(nums, p) == 1

    nums = [6, 3, 5, 2]
    p = 9
    assert Solution().minSubarray(nums, p) == 2

    nums = [1, 2, 3]
    p = 3
    assert Solution().minSubarray(nums, p) == 0


if __name__ == '__main__':
    main()
