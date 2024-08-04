from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


def main():
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    assert Solution().canBeEqual(target, arr) is True

    target = [7]
    arr = [7]
    assert Solution().canBeEqual(target, arr) is True

    target = [3, 7, 9]
    arr = [3, 7, 11]
    assert Solution().canBeEqual(target, arr) is False


if __name__ == '__main__':
    main()
