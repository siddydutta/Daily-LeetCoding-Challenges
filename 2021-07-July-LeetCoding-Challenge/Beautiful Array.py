# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Time Complexity: O(nlogn) '''
    def __split(self, array: List[int]) -> List[int]:
        # Base case
        if len(array) <= 2:
            return array
        even = array[0::2]  # Even indexed numbers
        odd = array[1::2]   # Odd indexed numbers
        return self.__split(even) + self.__split(odd)

    def beautifulArray(self, n: int) -> List[int]:
        return self.__split(list(range(1, n+1)))


def isBeautifulArray(array: List[int], n: int) -> bool:
    for i in range(n-1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                if array[k] * 2 == array[i] + array[j]:
                    return False
    return True


def main():
    for n in range(1, 100):
        try:
            assert isBeautifulArray(Solution().beautifulArray(n), n)
        except AssertionError:
            raise


if __name__ == '__main__':
    main()
