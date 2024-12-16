from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def getFinalState(
            self, nums: List[int], k: int, multiplier: int
    ) -> List[int]:
        nums = [(num, idx) for idx, num in enumerate(nums)]
        heapify(nums)
        for _ in range(k):
            num, idx = heappop(nums)
            num *= multiplier
            heappush(nums, (num, idx))
        result = [None] * len(nums)
        for num, idx in nums:
            result[idx] = num
        return result


def main():
    nums = [2, 1, 3, 5, 6]
    k = 5
    multplier = 2
    assert Solution().getFinalState(nums, k, multplier) == [8, 4, 6, 5, 6]

    nums = [1, 2]
    k = 3
    multiplier = 4
    assert Solution().getFinalState(nums, k, multiplier) == [16, 8]


if __name__ == '__main__':
    main()
