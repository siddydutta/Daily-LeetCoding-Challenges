# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ''' Solution based on prefix-sum and hashtable. '''
        prefix_sums = accumulate(nums)
        s_map = defaultdict(int)
        s_map[0] = 1  # For prefix sums equal to k
        ans = 0

        for s in prefix_sums:
            if s-k in s_map:  # Check if there is a prefix sum that gives diff
                ans += s_map[s-k]
            s_map[s] += 1
        return ans


def main():
    nums = [1, 1, 1]
    k = 2
    assert Solution().subarraySum(nums, k) == 2

    nums = [1, 2, 3]
    k = 3
    assert Solution().subarraySum(nums, k) == 2


if __name__ == '__main__':
    main()
