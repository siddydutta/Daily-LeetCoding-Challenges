from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        size = sum(nums)
        # extend array with window size to handle circular array
        nums.extend(nums[:size])

        # zeros in the window is = size - number of ones
        curr_zeros = size - sum(nums[:size])
        # swaps are the number of zeros in the window
        min_swaps = curr_zeros
        for i in range(1, len(nums)-size+1):
            # handle element leaving window
            curr_zeros += nums[i-1]
            # handle elment entering window
            curr_zeros -= nums[i+size-1]
            min_swaps = min(min_swaps, curr_zeros)

        return min_swaps


def main():
    nums = [0, 1, 0, 1, 1, 0, 0]
    assert Solution().minSwaps(nums) == 1

    nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    assert Solution().minSwaps(nums) == 2

    nums = [1, 1, 0, 0, 1]
    assert Solution().minSwaps(nums) == 0


if __name__ == '__main__':
    main()
