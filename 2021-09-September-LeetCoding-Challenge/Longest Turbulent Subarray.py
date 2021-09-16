# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def __compare(self, num1: int, num2: int) -> int:
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        else:
            return 0

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        start_ptr, end_ptr = 0, 1
        max_size = 1
        valid = True  # Flag that checks if comparison is flipped
        old_slope = 0

        while end_ptr < len(arr):
            new_slope = self.__compare(arr[end_ptr-1], arr[end_ptr])
            if new_slope == 0 or new_slope == old_slope:
                valid = False
            end_ptr += 1

            while not valid:
                if new_slope == 0:
                    start_ptr = end_ptr - 1
                else:
                    start_ptr = end_ptr - 2
                valid = True

            old_slope = new_slope
            max_size = max(max_size, end_ptr - start_ptr)

        return max_size


def main():
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    assert Solution().maxTurbulenceSize(arr) == 5

    arr = [4, 8, 12, 16]
    assert Solution().maxTurbulenceSize(arr) == 2

    arr = [100]
    assert Solution().maxTurbulenceSize(arr) == 1


if __name__ == '__main__':
    main()
