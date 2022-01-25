# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ''' Straighforward O(n) solution without sorting. '''
        n, ptr = len(arr), int()
        # Check strictly increasing
        while ptr+1 < n and arr[ptr] < arr[ptr+1]:
            ptr += 1
        # Check peak position, it cannot be first or last
        if ptr == 0 or ptr == n-1:
            return False
        # Check strictly decreasing
        while ptr+1 < n and arr[ptr] > arr[ptr+1]:
            ptr += 1
        return ptr == n-1  # Whether pointer has reached the end


def main():
    arr = [2, 1]
    assert not Solution().validMountainArray(arr)

    arr = [3, 5, 5]
    assert not Solution().validMountainArray(arr)

    arr = [0, 3, 2, 1]
    assert Solution().validMountainArray(arr)


if __name__ == '__main__':
    main()
