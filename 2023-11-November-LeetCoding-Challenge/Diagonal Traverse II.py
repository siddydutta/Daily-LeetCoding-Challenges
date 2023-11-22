from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        elements = list()
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                elements.append((i+j, -i, num))
        elements.sort()
        return [num for s, row, num in elements]


def main():
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().findDiagonalOrder(nums) == [1, 4, 2, 7, 5, 3, 8, 6, 9]

    nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    assert Solution().findDiagonalOrder(nums) == [1, 6, 2, 8, 7, 3, 9, 4, 12,
                                                  10, 5, 13, 11, 14, 15, 16]


if __name__ == '__main__':
    main()
