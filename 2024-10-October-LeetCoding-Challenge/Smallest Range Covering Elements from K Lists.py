from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heap)

        ans = [-inf, inf]
        right = max(row[0] for row in nums)
        while heap:
            left, i, j = heappop(heap)
            if right-left < ans[1]-ans[0]:
                ans = [left, right]
            if j+1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heappush(heap, (v, i, j+1))


def main():
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    assert Solution().smallestRange(nums) == [20, 24]

    nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert Solution().smallestRange(nums) == [1, 1]


if __name__ == '__main__':
    main()
