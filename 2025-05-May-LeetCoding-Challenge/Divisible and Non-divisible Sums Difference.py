class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (n * (n + 1) // 2) - (m * (n // m) * (n // m + 1))


def main():
    n = 10
    m = 3
    assert Solution().differenceOfSums(n, m) == 19

    n = 5
    m = 6
    assert Solution().differenceOfSums(n, m) == 15

    n = 5
    m = 1
    assert Solution().differenceOfSums(n, m) == -15


if __name__ == '__main__':
    main()
