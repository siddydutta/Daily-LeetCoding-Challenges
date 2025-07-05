from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counter = Counter(arr)
        result = -1
        for num, freq in counter.items():
            if num == freq:
                result = max(result, num)
        return result


def main():
    arr = [2, 2, 3, 4]
    assert Solution().findLucky(arr) == 2

    arr = [1, 2, 2, 3, 3, 3]
    assert Solution().findLucky(arr) == 3

    arr = [2, 2, 2, 3, 3]
    assert Solution().findLucky(arr) == -1


if __name__ == '__main__':
    main()
