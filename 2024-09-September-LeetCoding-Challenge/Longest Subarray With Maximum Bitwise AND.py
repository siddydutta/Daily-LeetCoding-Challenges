from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        curr_length, max_length = 0, 1
        for num in nums:
            if num == max_num:
                curr_length += 1
            else:
                curr_length = 0
            max_length = max(max_length, curr_length)
        return max_length


def main():
    nums = [1, 2, 3, 3, 2, 2]
    assert Solution().longestSubarray(nums) == 2

    nums = [1, 2, 3, 4]
    assert Solution().longestSubarray(nums) == 1


if __name__ == '__main__':
    main()
