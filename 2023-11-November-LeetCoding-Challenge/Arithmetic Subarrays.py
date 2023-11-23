from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic_sequence(start: int, end: int) -> bool:
            arr = sorted(nums[start:end+1])
            diff = arr[1] - arr[0]
            return all(arr[i+1] - arr[i] == diff for i in range(len(arr)-1))
        return [is_arithmetic_sequence(left, right) for left, right in zip(l, r)]


def main():
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    assert Solution().checkArithmeticSubarrays(nums, l, r) == [True, False, True]

    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l = [0, 1, 6, 4, 8, 7]
    r = [4, 4, 9, 7, 9, 10]
    assert Solution().checkArithmeticSubarrays(nums, l, r) == [False, True, False, False, True, True]


if __name__ == '__main__':
    main()
