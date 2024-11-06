from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max, prev_count = 0, 0
        curr_min, curr_max = 0, 0
        for num in nums:
            count = num.bit_count()
            if count == prev_count:
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)
            elif curr_min < prev_max:
                return False
            else:
                prev_max = curr_max
                curr_min, curr_max = num, num
                prev_count = count
        return curr_min >= prev_max


def main():
    nums = [8, 4, 2, 30, 15]
    assert Solution().canSortArray(nums) is True

    nums = [1, 2, 3, 4, 5]
    assert Solution().canSortArray(nums) is True

    nums = [3, 16, 8, 4, 2]
    assert Solution().canSortArray(nums) is False


if __name__ == '__main__':
    main()
