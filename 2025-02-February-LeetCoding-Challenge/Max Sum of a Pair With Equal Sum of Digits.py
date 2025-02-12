from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        max_sum = -1
        ds_map = defaultdict(int)
        for num in nums:
            s = sum(map(int, str(num)))
            if s in ds_map:
                max_sum = max(max_sum, ds_map[s] + num)
            ds_map[s] = max(ds_map[s], num)
        return max_sum


def main():
    nums = [18, 43, 36, 13, 7]
    assert Solution().maximumSum(nums) == 54

    nums = [10, 12, 19, 14]
    assert Solution().maximumSum(nums) == -1


if __name__ == '__main__':
    main()
