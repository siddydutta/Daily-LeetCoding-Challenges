class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            matches += n % 2
            n //= 2
            matches += n
        return matches


def main():
    n = 7
    assert Solution().numberOfMatches(n) == 6

    n = 14
    assert Solution().numberOfMatches(n) == 13


if __name__ == '__main__':
    main()
