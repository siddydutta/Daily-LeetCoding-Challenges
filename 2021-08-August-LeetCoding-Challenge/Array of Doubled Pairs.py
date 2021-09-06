# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    '''
    Solution based on sorting and hash table.
    Time Complexity: O(nlogn)
    Create pairs of n and 2*n.
    '''
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = Counter(arr)  # Map of array numbers and their counts
        arr.sort(key=abs)    # Sort numbers based on absolute values

        for num in arr:
            if freq[num] == 0:
                continue      # Number is already paired
            if freq[2*num] == 0:
                return False  # No available pair for number
            # Numbers are paired, so decrement frequencies
            freq[num] -= 1
            freq[2*num] -= 1

        return True


def main():
    arr = [3, 1, 3, 6]
    assert not Solution().canReorderDoubled(arr)

    arr = [4, -2, 2, -4]
    assert Solution().canReorderDoubled(arr)

    arr = [1, 2, 4, 16, 8, 4]
    assert not Solution().canReorderDoubled(arr)

    arr = [-33, 0]
    assert not Solution().canReorderDoubled(arr)


if __name__ == '__main__':
    main()
