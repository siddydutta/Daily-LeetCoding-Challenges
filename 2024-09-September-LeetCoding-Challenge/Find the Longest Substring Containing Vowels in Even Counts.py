class Solution:
    INDEX_MAP = {ch: i for i, ch in enumerate('aeiou')}

    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        mask = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in self.INDEX_MAP:
                # toggles the bit corresponding to the vowel
                mask ^= (1 << self.INDEX_MAP[ch])
            seen.setdefault(mask, i)
            # if mask is seen before, then substring between
            # then and now is valid (all vowels in even counts)
            max_len = max(max_len, i-seen[mask])
        return max_len


def main():
    s = 'eleetminicoworoep'
    assert Solution().findTheLongestSubstring(s) == 13

    s = 'leetcodeisgreat'
    assert Solution().findTheLongestSubstring(s) == 5

    s = 'bcbcbc'
    assert Solution().findTheLongestSubstring(s) == 6


if __name__ == '__main__':
    main()
