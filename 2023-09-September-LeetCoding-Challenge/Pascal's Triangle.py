from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle


def main():
    assert Solution().generate(5) == [[1],
                                      [1, 1],
                                      [1, 2, 1],
                                      [1, 3, 3, 1],
                                      [1, 4, 6, 4, 1]]

    assert Solution().generate(1) == [[1]]


if __name__ == '__main__':
    main()
