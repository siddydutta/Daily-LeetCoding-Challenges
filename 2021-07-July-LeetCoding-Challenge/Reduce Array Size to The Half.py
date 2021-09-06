# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        req = n // 2

        # Obtain a sorted frequency of digits in the array
        frequency = Counter(arr).most_common()
        result = 0

        while n > req:
            n -= frequency.pop(0)[1]  # Subtract max frequency count
            result += 1

        return result


def main():
    obj = Solution()

    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    assert obj.minSetSize(arr) == 2

    arr = [7, 7, 7, 7, 7, 7]
    assert obj.minSetSize(arr) == 1

    arr = [1, 9]
    assert obj.minSetSize(arr) == 1

    arr = [1000, 1000, 3, 7]
    assert obj.minSetSize(arr) == 1

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert obj.minSetSize(arr) == 5


if __name__ == '__main__':
    main()
