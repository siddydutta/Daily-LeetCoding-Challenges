from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = Counter(s).values()
        count, seen = int(), set()
        for freq in frequencies:
            while freq > 0 and freq in seen:
                freq -= 1
                count += 1
            seen.add(freq)
        return count


def main():
    s = "aab"
    assert Solution().minDeletions(s) == 0

    s = "aaabbbcc"
    assert Solution().minDeletions(s) == 2

    s = "ceabaacb"
    assert Solution().minDeletions(s) == 2


if __name__ == '__main__':
    main()
