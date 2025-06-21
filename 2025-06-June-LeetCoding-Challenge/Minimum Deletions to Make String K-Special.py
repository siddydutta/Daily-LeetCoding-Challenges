from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())
        freqs.sort()

        min_deletions = len(word)
        prefix_sum = 0
        for i in range(len(freqs)):
            deletions = prefix_sum
            for j in range(i + 1, len(freqs)):
                if freqs[j] > freqs[i] + k:
                    deletions += freqs[j] - (freqs[i] + k)
            min_deletions = min(min_deletions, deletions)
            prefix_sum += freqs[i]
        return min_deletions


def main():
    word = 'aabcaba'
    k = 0
    assert Solution().minimumDeletions(word, k) == 3

    word = 'dabdcbdcdcd'
    k = 2
    assert Solution().minimumDeletions(word, k) == 2

    word = 'aaabaaa'
    k = 2
    assert Solution().minimumDeletions(word, k) == 1


if __name__ == '__main__':
    main()
