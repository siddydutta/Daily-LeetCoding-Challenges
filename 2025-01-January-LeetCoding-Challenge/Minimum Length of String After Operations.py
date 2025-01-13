from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if c & 1 else 2 for c in Counter(s).values())


def main():
    s = 'abaacbcbb'
    assert Solution().minimumLength(s) == 5

    s = 'aa'
    assert Solution().minimumLength(s) == 2


if __name__ == '__main__':
    main()
