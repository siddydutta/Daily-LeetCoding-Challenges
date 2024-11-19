from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        curr_sum, max_sum = 0, 0
        for ptr, num in enumerate(nums):
            curr_sum += num
            freq[num] += 1
            if ptr >= k:
                prev = nums[ptr - k]
                curr_sum -= prev
                freq[prev] -= 1
                if freq[prev] == 0:
                    del freq[prev]
            if len(freq) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum


def main():
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    assert Solution().maximumSubarraySum(nums, k) == 15

    nums = [4, 4, 4]
    k = 3
    assert Solution().maximumSubarraySum(nums, k) == 0


if __name__ == '__main__':
    main()
