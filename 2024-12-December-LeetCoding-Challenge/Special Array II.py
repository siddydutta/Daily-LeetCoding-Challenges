from typing import List


class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        ps = [0] * n
        for i in range(1, n):
            ps[i] = ps[i-1] + (nums[i-1] % 2 == nums[i] % 2)
        return [ps[p2]-ps[p1] == 0 for p1, p2 in queries]


def main():
    nums = [3, 4, 1, 2, 6]
    queries = [[0, 4]]
    assert Solution().isArraySpecial(nums, queries) == [False]

    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]
    assert Solution().isArraySpecial(nums, queries) == [False, True]


if __name__ == '__main__':
    main()
