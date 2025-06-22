class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        s += fill * (-len(s) % k)
        return [s[i: i + k] for i in range(0, len(s), k)]


def main():
    s = 'abcdefghi'
    k = 3
    fill = 'x'
    assert Solution().divideString(s, k, fill) == ['abc', 'def', 'ghi']

    s = 'abcdefghij'
    k = 3
    fill = 'x'
    assert Solution().divideString(s, k, fill) == ['abc', 'def', 'ghi', 'jxx']


if __name__ == '__main__':
    main()
