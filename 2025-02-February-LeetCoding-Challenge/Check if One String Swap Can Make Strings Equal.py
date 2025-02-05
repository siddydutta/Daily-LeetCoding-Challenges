class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        s1_freq, s2_freq = [0] * 26, [0] * 26
        for ch1, ch2 in zip(s1, s2):
            count += ch1 != ch2
            if count > 2:
                return False
            s1_freq[ord(ch1)-ord('a')] += 1
            s2_freq[ord(ch2)-ord('a')] += 1
        return s1_freq == s2_freq


def main():
    s1 = 'bank'
    s2 = 'kanb'
    assert Solution().areAlmostEqual(s1, s2) is True

    s1 = 'attack'
    s2 = 'defend'
    assert Solution().areAlmostEqual(s1, s2) is False

    s1 = 'kelb'
    s2 = 'kelb'
    assert Solution().areAlmostEqual(s1, s2) is True


if __name__ == '__main__':
    main()
