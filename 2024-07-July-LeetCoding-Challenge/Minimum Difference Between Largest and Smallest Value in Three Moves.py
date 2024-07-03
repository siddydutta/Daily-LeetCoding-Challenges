from heapq import nlargest, nsmallest
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # remove 3 elements between the 3 smallest
        # and 3 largest values in the array
        if len(nums) <= 4:
            return 0

        max_4 = nlargest(4, nums)
        min_4 = nsmallest(4, nums)

        return min([
            max_4[0] - min_4[3],  # kill smallest 3
            max_4[1] - min_4[2],  # kill 1 biggest, 2 smallest
            max_4[2] - min_4[1],  # kill 1 smallest, 2 biggest
            max_4[3] - min_4[0],  # kill biggest 3

        ])


def main():
    nums = [5, 3, 2, 4]
    assert Solution().minDifference(nums) == 0

    nums = [1, 5, 0, 10, 14]
    assert Solution().minDifference(nums) == 1

    nums = [3, 100, 20]
    assert Solution().minDifference(nums) == 0


if __name__ == '__main__':
    main()
