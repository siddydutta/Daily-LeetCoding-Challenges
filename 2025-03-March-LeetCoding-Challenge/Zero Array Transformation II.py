class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        curr_sum, k = 0, 0
        for i, num in enumerate(nums):
            while curr_sum + prefix_sum[i] < num:
                if k == len(queries):
                    return -1
                left, right, val = queries[k]
                if i <= right:
                    prefix_sum[max(i, left)] += val
                    prefix_sum[right + 1] -= val
                k += 1
            curr_sum += prefix_sum[i]
        return k


def main():
    nums = [2, 0, 2]
    queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    assert Solution().minZeroArray(nums, queries) == 2

    nums = [4, 3, 2, 1]
    queries = [[1, 3, 2], [0, 2, 1]]
    assert Solution().minZeroArray(nums, queries) == -1


if __name__ == '__main__':
    main()
