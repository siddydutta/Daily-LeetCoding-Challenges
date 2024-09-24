from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        prefixes = set()
        for num in arr1:
            for i in range(len(num)):
                prefixes.add(num[:i+1])
        max_len = 0
        for num in arr2:
            for i in range(max_len, len(num)):
                if num[:i+1] in prefixes:
                    max_len += 1
        return max_len


def main():
    arr1 = [1, 10, 100]
    arr2 = [1000]
    assert Solution().longestCommonPrefix(arr1, arr2) == 3

    arr1 = [1, 2, 3]
    arr2 = [4, 4, 4]
    assert Solution().longestCommonPrefix(arr1, arr2) == 0


if __name__ == '__main__':
    main()
