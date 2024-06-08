from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums_map = {0: -1}
        curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum = (curr_sum + num) % k
            if curr_sum in sums_map:
                if idx - sums_map[curr_sum] > 1:
                    # idx diff should be at least 2
                    return True
            else:
                sums_map[curr_sum] = idx
        return False


def main():
    nums = [23, 2, 4, 6, 7]
    k = 6
    assert Solution().checkSubarraySum(nums, k) is True

    nums = [23, 2, 6, 4, 7]
    k = 6
    assert Solution().checkSubarraySum(nums, k) is True

    nums = [23, 2, 6, 4, 7]
    k = 13
    assert Solution().checkSubarraySum(nums, k) is False


if __name__ == '__main__':
    main()
