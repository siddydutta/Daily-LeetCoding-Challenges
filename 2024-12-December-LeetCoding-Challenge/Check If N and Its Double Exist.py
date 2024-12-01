from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elements = set()
        for n in arr:
            if n*2 in elements or (n % 2 == 0 and n//2 in elements):
                return True
            elements.add(n)
        return False


def main():
    arr = [10, 2, 5, 3]
    assert Solution().checkIfExist(arr) is True

    arr = [3, 1, 7, 11]
    assert Solution().checkIfExist(arr) is False


if __name__ == '__main__':
    main()
