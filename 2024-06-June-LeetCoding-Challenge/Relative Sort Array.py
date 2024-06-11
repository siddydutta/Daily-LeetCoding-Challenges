from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        freq = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num]*freq.pop(num))
        for num, count in freq.items():
            res.extend([num]*count)
        return res


def main():
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    assert Solution().relativeSortArray(arr1, arr2) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]  # noqa: E501

    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]
    assert Solution().relativeSortArray(arr1, arr2) == [22, 28, 8, 6, 17, 44]


if __name__ == '__main__':
    main()
