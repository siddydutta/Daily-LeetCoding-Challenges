from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        # sort by asc freq, then desc value
        return sorted(nums, key=lambda n: (freqs[n], -n))


def main():
    nums = [1, 1, 2, 2, 2, 3]
    assert Solution().frequencySort(nums) == [3, 1, 1, 2, 2, 2]

    nums = [2, 3, 1, 3, 2]
    assert Solution().frequencySort(nums) == [1, 3, 3, 2, 2]

    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    assert Solution().frequencySort(nums) == [5, -1, 4, 4, -6, -6, 1, 1, 1]


if __name__ == '__main__':
    main()
