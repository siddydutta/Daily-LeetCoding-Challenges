from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(Counter(word).values(), reverse=True)
        pushes = 0
        for mul, freq in enumerate(freqs, start=8):
            pushes += freq * (mul//8)
        return pushes


def main():
    word = 'abcde'
    assert Solution().minimumPushes(word) == 5

    word = 'xyzxyzxyzxyz'
    assert Solution().minimumPushes(word) == 12

    word = 'aabbccddeeffgghhiiiiii'
    assert Solution().minimumPushes(word) == 24


if __name__ == '__main__':
    main()
