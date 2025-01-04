from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = Counter(s)  # frequency of right string
        seen = set()  # seen characters of left string
        subs = set()  # set of palindromic subsequences
        for char in s:
            freq[char] -= 1
            for ch in seen:
                if freq[ch] > 0:
                    subs.add((ch, char))  # same as ch+char+ch
            seen.add(char)
        return len(subs)


def main():
    s = 'aabca'
    assert Solution().countPalindromicSubsequence(s) == 3

    s = 'adc'
    assert Solution().countPalindromicSubsequence(s) == 0

    s = 'bbcbaba'
    assert Solution().countPalindromicSubsequence(s) == 4


if __name__ == '__main__':
    main()
