class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n-1) // 2


def main():
    n = 1
    assert Solution().coloredCells(n) == 1

    n = 2
    assert Solution().coloredCells(n) == 5


if __name__ == '__main__':
    main()
