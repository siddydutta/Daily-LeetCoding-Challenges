from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        for i, num in enumerate(sorted(list(set(arr))), start=1):
            ranks[num] = i
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr


def main():
    arr = [40, 10, 20, 30]
    assert Solution().arrayRankTransform(arr) == [4, 1, 2, 3]

    arr = [100, 100, 100]
    assert Solution().arrayRankTransform(arr) == [1, 1, 1]

    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    assert Solution().arrayRankTransform(arr) == [5, 3, 4, 2, 8, 6, 7, 1, 3]


if __name__ == '__main__':
    main()
