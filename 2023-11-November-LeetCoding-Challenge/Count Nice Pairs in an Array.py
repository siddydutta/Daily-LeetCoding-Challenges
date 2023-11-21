from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq, count = defaultdict(int), 0
        for i in range(len(nums)):
            num = nums[i] - int(str(nums[i])[::-1])
            count += freq[num]
            freq[num] += 1
        return count % (10**9+7)


def main():
    nums = [42, 11, 1, 97]
    assert Solution().countNicePairs(nums) == 2

    nums = [13, 10, 35, 24, 76]
    assert Solution().countNicePairs(nums) == 4


if __name__ == '__main__':
    main()
