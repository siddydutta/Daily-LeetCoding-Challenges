class Solution:
    def minChanges(self, s: str) -> int:
        return sum([s[i] != s[i+1] for i in range(0, len(s), 2)])


def main():
    s = '1001'
    assert Solution().minChanges(s) == 2

    s = '10'
    assert Solution().minChanges(s) == 1

    s = '0000'
    assert Solution().minChanges(s) == 0


if __name__ == '__main__':
    main()
