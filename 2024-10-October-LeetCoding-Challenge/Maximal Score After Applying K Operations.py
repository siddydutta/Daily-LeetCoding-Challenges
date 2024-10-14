from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -1*x, nums))
        heapify(nums)
        score = 0
        for _ in range(k):
            max_element = -heappop(nums)
            score += max_element
            heappush(nums, -ceil(max_element/3))
        return score


def main():
    nums = [10, 10, 10, 10, 10]
    k = 5
    assert Solution().maxKelements(nums, k) == 50

    nums = [1, 10, 3, 3, 3]
    k = 3
    assert Solution().maxKelements(nums, k) == 17


if __name__ == '__main__':
    main()
