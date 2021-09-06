# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]  # Initial Row
        for i in range(1, numRows):
            row = list()
            row.append(1)  # Starting 1
            for j in range(1, len(result[i-1])):
                # Addition of previous row numbers
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)  # Ending 1
            result.append(row)
        return result


def main():
    obj = Solution()
    num_rows = 5
    assert obj.generate(num_rows) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                                      [1, 4, 6, 4, 1]]

    num_rows = 1
    assert obj.generate(num_rows) == [[1]]


if __name__ == '__main__':
    main()
