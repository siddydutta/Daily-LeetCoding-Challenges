from itertools import accumulate


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        diff_array = [0] * (len(nums) + 1)
        for start, finish in queries:
            diff_array[start] += 1
            diff_array[min(finish + 1, len(nums))] -= 1
        prefix_sum = list(accumulate(diff_array))[:-1]
        return all(num <= curr_sum for num, curr_sum in zip(nums, prefix_sum))


def main():
    nums = [1, 0, 1]
    queries = [[0, 2]]
    assert Solution().isZeroArray(nums, queries) is True

    nums = [4, 3, 2, 1]
    queries = [[1, 3], [0, 2]]
    assert Solution().isZeroArray(nums, queries) is False


if __name__ == '__main__':
    main()
