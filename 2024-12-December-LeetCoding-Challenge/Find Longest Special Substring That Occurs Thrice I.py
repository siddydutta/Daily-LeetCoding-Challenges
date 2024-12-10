from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        freq = defaultdict(int)
        for i in range(len(s)):
            length = 1
            freq[(s[i], length)] += 1
            for j in range(i, len(s)-1):
                if s[j] == s[j+1]:
                    length += 1
                    freq[(s[i], length)] += 1
                else:
                    break

        max_length = -1
        for key, value in freq.items():
            if value >= 3:
                max_length = max(max_length, key[1])
        return max_length


def main():
    s = 'aaaa'
    assert Solution().maximumLength(s) == 2

    s = 'abcdef'
    assert Solution().maximumLength(s) == -1

    s = 'abcaba'
    assert Solution().maximumLength(s) == 1


if __name__ == '__main__':
    main()
