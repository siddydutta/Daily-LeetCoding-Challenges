from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        j = len(arr) - 1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1

        i, res = 0, j
        while i < j and (i == 0 or arr[i-1] <= arr[i]):
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            res = min(res, j-i-1)
            i += 1
        return res


def main():
    arr = [1, 2, 3, 10, 4, 2, 3, 5]
    assert Solution().findLengthOfShortestSubarray(arr) == 3

    arr = [5, 4, 3, 2, 1]
    assert Solution().findLengthOfShortestSubarray(arr) == 4

    arr = [1, 2, 3]
    assert Solution().findLengthOfShortestSubarray(arr) == 0


if __name__ == '__main__':
    main()
