from itertools import product


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        total = 0
        duplicate = None
        seen = [False] * n**2

        for i, j in product(range(n), range(n)):
            num = grid[i][j]
            if seen[num-1]:
                duplicate = num
            else:
                total += num
                seen[num-1] = True

        expected = (n**2 * (n**2 + 1)) // 2
        return [duplicate, expected-total]


def main():
    grid = [[1, 3],
            [2, 2]]
    assert Solution().findMissingAndRepeatedValues(grid) == [2, 4]

    grid = [[9, 1, 7],
            [8, 9, 2],
            [3, 4, 6]]
    assert Solution().findMissingAndRepeatedValues(grid) == [9, 5]


if __name__ == '__main__':
    main()
