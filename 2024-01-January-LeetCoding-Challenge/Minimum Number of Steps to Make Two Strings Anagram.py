from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s, freq_t = Counter(s), Counter(t)
        steps = 0
        for ch, count in freq_s.items():
            if count > freq_t[ch]:
                steps += (count - freq_t[ch])
        return steps


def main():
    s = 'bab'
    t = 'aba'
    assert Solution().minSteps(s, t) == 1

    s = 'leetcode'
    t = 'practice'
    assert Solution().minSteps(s, t) == 5

    s = 'anagram'
    t = 'mangaar'
    assert Solution().minSteps(s, t) == 0


if __name__ == '__main__':
    main()
