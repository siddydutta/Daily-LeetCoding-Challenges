from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        threshold = 0.25 * len(arr)
        for num, count in freq.items():
            if count > threshold:
                return num
        return None


def main():
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    assert Solution().findSpecialInteger(arr) == 6

    arr = [1, 1]
    assert Solution().findSpecialInteger(arr) == 1


if __name__ == '__main__':
    main()
